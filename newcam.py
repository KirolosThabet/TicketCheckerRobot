import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import cv2
import numpy as np
import math
from pyzbar.pyzbar import decode


# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the video capture object for the camera
video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera
video_capture.set(3,320)
video_capture.set(4,240)
# Initialize the human count
human_count = 0
arr=[]
count=0
lastprint=""
qrCounter=0

with open('/home/pi/hngrb/dataList.txt') as file:
    myDataList=file.read().splitlines()
if __name__ == '__main__':
    speaker_pub = rospy.Publisher('chatter', String, queue_size=10)
    #led_pub = rospy.Publisher('/led/status', Bool, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    while True:
        # Capture frame-by-frame from the camera
        
        if count==200:
            break
        ret, frame = video_capture.read()
        frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
       
        #minNeighbors: This parameter specifies the number of neighbors a detected region should have to be considered a face. 
        
        # It helps filter out false positives. Higher values result in stricter face detection, reducing false positives but potentially missing some faces.

        #minSize: This parameter defines the minimum size of the detected face. Any region smaller than this size is ignored. 
        # It helps filter out noise or small objects that may not be actual faces. In this case, (30, 30) specifies that any face smaller 
        # than 30x30 pixels will be ignored.

        # Update the human count
        human_count = len(faces)
        arr.append(human_count)
        count+=1
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the human count
        cv2.putText(frame, f"Human count: {human_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the frame with the human count and face detection
        cv2.imshow("Face Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    
# Release the video capture object and close any open windows
    speaker_pub.publish("facial detection is done")
    # Release the video capture object and close any open windows
    average_pass=sum(arr)/len(arr)
    print('print:',average_pass)
    average_pass=math.ceil(average_pass)
    while True:
        ret, frame=video_capture.read()
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
                    rate.sleep()
        
        cv2.imshow('Following Camera',frame)
        cv2.waitKey(1)
video_capture.release()
cv2.destroyAllWindows()
