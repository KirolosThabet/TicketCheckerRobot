import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
Servo_pin=18
GPIO.setup(Servo_pin, GPIO.OUT)
pwm=GPIO.PWM(Servo_pin, 50)
pwm.start(0)
try:
    while True:
        pwmpercent=float(input('pwm%'))
        pwm.ChangeDutyCycle(pwmpercent)
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()