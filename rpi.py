import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# pin setup
left_one = 9
left_two = 10
right_one = 19
right_two = 26
GPIO.setup(left_one,GPIO.OUT)
GPIO.setup(left_two,GPIO.OUT)
GPIO.setup(right_one,GPIO.OUT)
GPIO.setup(right_two,GPIO.OUT)
def forward():
    GPIO.output(left_one,False)
    GPIO.output(left_two,True)
    GPIO.output(right_one,True)
    GPIO.output(right_two,False)
def stop():
    GPIO.output(left_one,False)
    GPIO.output(left_two,False)
    GPIO.output(right_one,False)
    GPIO.output(right_two,False)
def left():
    GPIO.output(left_one,True)
    GPIO.output(left_two,True)
    GPIO.output(right_one,True)
    GPIO.output(right_one,False)
def right():
    GPIO.output(left_one,False)
    GPIO.output(left_two,True)
    GPIO.output(right_one,False)
    GPIO.output(right_two,False)
forward()
time.sleep(10)
left()
time.sleep(5)
forward()