import rospy
from std_msgs.msg import String,Int
import RPi.GPIO as GPIO
import time
IrRight=1
IrLeft=1
IrMid=1
d=1000
# declare IR sensor Pins
IrRight_pin = 14
IrLeft_pin= 15
IrMid_pin= 18

#declare Ultrasonic pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IrRight_pin, GPIO.IN)
GPIO.setup(IrLeft_pin, GPIO.IN)
GPIO.setup(IrMid_pin, GPIO.IN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
     # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time() 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

def Walking():
#make it for Raspberry pi
#Motor_states = 2 right wheel will turn
#Motor_states = 3 left  wheel will turn
    while True:
        Motor_states=1
        #if(IrMid==0 and IrRight==1 and IrLeft==1):
         #   Motor_states = 1
        IrRight=GPIO.input(IrRight_pin)
        IrLeft=GPIO.input(IrLeft_pin)
        IrMid=GPIO.input(IrMid_pin)
        d=distance()
        print('IR1:',IrRight)
        if(IrMid==0 and IrRight==1 and IrLeft==0):
            Motor_states = 2 
        elif(IrMid==0 and IrRight==0 and IrLeft==1):
            Motor_states = 3
        elif(IrMid==0 and IrRight==0 and IrLeft==0):
            Motor_states=0
            Motors_pub.publish(int(Motor_states))
            break
        Motors_pub.publish(int(Motor_states))


if __name__ == '__main__':
    Speaker_pub = rospy.Publisher('chatter', String, queue_size=10)
    Motors_pub = rospy.Publisher('Motors_States', Int, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    try:
        while True:
            success, img=cap.read()
            ###########################################
            Walking()
            ###########################################
            #HumanDetection()

            ########################################### 
            #QRCodeDetect(img,n)
            """ for qrcode in decode(img):
                qrdata=qrcode.data.decode('utf-8')
                print(qrdata)
                points=np.array([qrcode.polygon],np.int32)
                points=points.reshape((-1,1,2))
                cv2.polylines(img,[points],True,(0,255,0),5)
                rect_points=qrcode.rect
                cv2.putText(img,qrdata,(rect_points[0],rect_points[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
                if(qrdata!=lastprint):
                    lastprint=qrdata
                    Speaker_pub.publish(lastprint)
                    rate.sleep()
 """
            cv2.imshow('Following Camera',img)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        GPIO.cleanup()





    while True:
        ret, frame=cap.read()
        frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        if(qrCounter==average_pass):
            break
        for qrcode in decode(frame):
            qrdata=qrcode.data.decode('utf-8')
            #qrdata=qrdata[5]
            print(qrdata)
            if qrdata in myDataList:
                points=np.array([qrcode.polygon],np.int32)
                points=points.reshape((-1,1,2))
                
                cv2.polylines(frame,[points],True,(0,255,0),5)
                rect_points=qrcode.rect
                cv2.putText(frame,qrdata,(rect_points[0],rect_points[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
                if(qrdata!=lastprint):
                    qrCounter+=1
                    lastprint=qrdata
                    speaker_pub.publish(lastprint)
                    led_pub.publish(True)
                    rate.sleep()
        
        cv2.imshow('Following Camera',frame)
        cv2.waitKey(1)
