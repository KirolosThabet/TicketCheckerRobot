import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import rospy
from std_msgs.msg import Int32
import math

i = Int32()
i = 111
state = 0
x = 0

def RED():
   global i
   i = 100 + math.remainder(i,100)
   print(i)

def GREEN():
   global i
   i = 200 + math.remainder(i,100)
   print(i)

def GREY():
   global i
   i = 300 + math.remainder(i,100)
   print(i)

def WHITE():
   global i
   i = 400 + math.remainder(i,100)
   print(i)

def NEXT():
   global state
   global x
   global i
   if state == 0:
      x = x+1
      if x == 17:
         x=1
         i = i//100
         i = i*100+11
      elif x == 1:
         i = i//100
         i = i*100+11
      elif x == 2:
         i = i//100
         i = i*100+12   
      elif x == 3:
         i = i//100
         i = i*100+13          
      elif x == 4:
         i = i//100
         i = i*100+14 
      elif x == 5:
         i = i//100
         i = i*100+21 
      elif x == 6:
         i = i//100
         i = i*100+22 
      elif x == 7:
         i = i//100
         i = i*100+23 
      elif x == 8:
         i = i//100
         i = i*100+24 
      elif x == 9:
         i = i//100
         i = i*100+31 
      elif x == 10:
         i = i//100
         i = i*100+32 
      elif x == 11:
         i = i//100
         i = i*100+ 33
      elif x == 12:
         i = i//100
         i = i*100+34 
      elif x == 13:
         i = i//100
         i = i*100+41 
      elif x == 14:
         i = i//100
         i = i*100+42 
      elif x == 15:
         i = i//100
         i = i*100+43 
      elif x == 16:
         i = i//100
         i = i*100+44

      if i == 111:
         window.A1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 112:
           window.A2.setStyleSheet("QLabel { background-color : red; color : black; }") 
      elif i == 113:
           window.A3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 114:
           window.A4.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 121:
           window.B1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 122:
           window.B2.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 123:
           window.B3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 124:
           window.B4.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 131:
           window.C1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 132:
           window.C2.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 133:
           window.C3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 134:
           window.C4.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 141:
           window.D1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 142:
           window.D2.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 143:
           window.D3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 144:
           window.D4.setStyleSheet("QLabel { background-color : red; color : black; }")
      if i == 211:
         window.A1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 212:
           window.A2.setStyleSheet("QLabel { background-color : green; color : black; }") 
      elif i == 213:
           window.A3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 214:
           window.A4.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 221:
           window.B1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 222:
           window.B2.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 223:
           window.B3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 224:
           window.B4.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 231:
           window.C1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 232:
           window.C2.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 233:
           window.C3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 234:
           window.C4.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 241:
           window.D1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 242:
           window.D2.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 243:
           window.D3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 244:
           window.D4.setStyleSheet("QLabel { background-color : green; color : black; }")
      if i == 311:
         window.A1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 312:
           window.A2.setStyleSheet("QLabel { background-color : grey; color : black; }") 
      elif i == 313:
           window.A3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 314:
           window.A4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 321:
           window.B1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 322:
           window.B2.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 323:
           window.B3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 324:
           window.B4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 331:
           window.C1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 332:
           window.C2.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 333:
           window.C3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 334:
           window.C4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 341:
           window.D1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 342:
           window.D2.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 343:
           window.D3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 344:
           window.D4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      if i == 411:
         window.A1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 412:
           window.A2.setStyleSheet("QLabel { background-color : white; color : black; }") 
      elif i == 413:
           window.A3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 414:
           window.A4.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 421:
           window.B1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 422:
           window.B2.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 423:
           window.B3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 424:
           window.B4.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 431:
           window.C1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 432:
           window.C2.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 433:
           window.C3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 434:
           window.C4.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 441:
           window.D1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 442:
           window.D2.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 443:
           window.D3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 444:
           window.D4.setStyleSheet("QLabel { background-color : white; color : black; }")
      window.DisplaySeat.display(math.remainder(i,100))     


def SPEED(data):
    if data == 1:
        window.pushButton_2.setStyleSheet("QPushButton { background-color : yellow; color : black; }")
        window.pushButton_2.setText("RESUME")
        pub.publish(0)
    else:
        window.pushButton_2.setStyleSheet("QPushButton { background-color : red; color : black; }")
        window.pushButton_2.setText("STOP")
        pub.publish(1)        


def Manual():
    global state
    state=0
    window.LEDM.setStyleSheet("QLabel { background-color : orange; color : black; }")
    window.LEDA.setStyleSheet("QLabel { background-color : white; color : black; }")
    


def Auto():
    global state
    state=1
    window.LEDA.setStyleSheet("QLabel { background-color : orange; color : black; }")
    window.LEDM.setStyleSheet("QLabel { background-color : white; color : black; }")    

def SEND():
     rospy.Subscriber("/subs",Int32,callback)
     window.LEDA.setStyleSheet("QLabel { background-color : orange; color : black; }")
    # num_msg=Int32()
     #num_msg.data=random.randint(0,10)
     #pub.publish(num_msg)
     
def callback(data):
      global i
      i=data.data
      #print(i)
      if i == 111:
         window.A1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 112:
           window.A2.setStyleSheet("QLabel { background-color : red; color : black; }") 
      elif i == 113:
           window.A3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 114:
           window.A4.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 121:
           window.B1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 122:
           window.B2.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 123:
           window.B3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 124:
           window.B4.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 131:
           window.C1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 132:
           window.C2.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 133:
           window.C3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 134:
           window.C4.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 141:
           window.D1.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 142:
           window.D2.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 143:
           window.D3.setStyleSheet("QLabel { background-color : red; color : black; }")
      elif i == 144:
           window.D4.setStyleSheet("QLabel { background-color : red; color : black; }")
      if i == 211:
         window.A1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 212:
           window.A2.setStyleSheet("QLabel { background-color : green; color : black; }") 
      elif i == 213:
           window.A3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 214:
           window.A4.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 221:
           window.B1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 222:
           window.B2.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 223:
           window.B3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 224:
           window.B4.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 231:
           window.C1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 232:
           window.C2.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 233:
           window.C3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 234:
           window.C4.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 241:
           window.D1.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 242:
           window.D2.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 243:
           window.D3.setStyleSheet("QLabel { background-color : green; color : black; }")
      elif i == 244:
           window.D4.setStyleSheet("QLabel { background-color : green; color : black; }")
      if i == 311:
         window.A1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 312:
           window.A2.setStyleSheet("QLabel { background-color : grey; color : black; }") 
      elif i == 313:
           window.A3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 314:
           window.A4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 321:
           window.B1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 322:
           window.B2.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 323:
           window.B3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 324:
           window.B4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 331:
           window.C1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 332:
           window.C2.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 333:
           window.C3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 334:
           window.C4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 341:
           window.D1.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 342:
           window.D2.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 343:
           window.D3.setStyleSheet("QLabel { background-color : grey; color : black; }")
      elif i == 344:
           window.D4.setStyleSheet("QLabel { background-color : grey; color : black; }")
      if i == 411:
         window.A1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 412:
           window.A2.setStyleSheet("QLabel { background-color : white; color : black; }") 
      elif i == 413:
           window.A3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 414:
           window.A4.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 421:
           window.B1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 422:
           window.B2.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 423:
           window.B3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 424:
           window.B4.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 431:
           window.C1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 432:
           window.C2.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 433:
           window.C3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 434:
           window.C4.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 441:
           window.D1.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 442:
           window.D2.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 443:
           window.D3.setStyleSheet("QLabel { background-color : white; color : black; }")
      elif i == 444:
           window.D4.setStyleSheet("QLabel { background-color : white; color : black; }")
      #ral=real()     
      window.DisplaySeat.display(math.remainder(i,100))      
          

rospy.init_node("gui")
rospy.loginfo("starting node one.. ")
pub=rospy.Publisher("/num",Int32,queue_size=10)
r=rospy.Rate(10)


app = QtWidgets.QApplication(sys.argv)

loader = QUiLoader()


window = loader.load("firstgui.ui",None)
window.setWindowTitle("GUI Application")


window.RED.clicked.connect(RED)
window.GREEN.clicked.connect(GREEN)
window.GREY.clicked.connect(GREY)
window.WHITE.clicked.connect(WHITE)
window.SWITCH.clicked.connect(NEXT)
window.pushButton_2.toggled.connect(SPEED)
window.MANUAL.clicked.connect(Manual)
window.AUTO.clicked.connect(Auto)
window.pushButton.clicked.connect(SEND)


window.show()
app.exec()