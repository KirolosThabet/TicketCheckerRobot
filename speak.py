import rospy
from std_msgs.msg import String
import os
import time
from playsound import playsound
from gtts import gTTS
from pygame import mixer
mixer.init()

def speak(text):
    tts= gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    mixer.music.load("/home/pi/hngrb/voice.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    while mixer.music.get_busy()==True:
        continue

def callback(msg):
    text=msg.data #"Egypt Railways wish you a nice trip on"+msg.data
    speak(text)

if __name__ == '__main__':
    rospy.init_node('speaker', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    while not rospy.is_shutdown():
        rospy.spin()
 