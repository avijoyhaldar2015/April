import Adafruit_BBIO.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Fetch the service account key JSON file contents
cred = credentials.Certificate('april-1546223003954-firebase-adminsdk-w4per-0ee9a80d84.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://april-1546223003954.firebaseio.com/'
})
ref=db.reference('/April/').update({'bot_downlink' : '1'})
motor1_pin1="P8_12"
motor1_pin2="P8_14"
motor2_pin1="P9_23"
motor2_pin2="P9_25"
GPIO.setup(motor1_pin1,GPIO.OUT)
GPIO.setup(motor1_pin2,GPIO.OUT)
GPIO.setup(motor2_pin1,GPIO.OUT)
GPIO.setup(motor2_pin2,GPIO.OUT)
def forward():
        GPIO.output(motor1_pin1,GPIO.LOW)
        GPIO.output(motor1_pin2,GPIO.HIGH)
        GPIO.output(motor2_pin1,GPIO.HIGH)
        GPIO.output(motor2_pin2,GPIO.LOW)
def left():
        GPIO.output(motor1_pin1,GPIO.HIGH)
        GPIO.output(motor1_pin2,GPIO.HIGH)
        GPIO.output(motor2_pin1,GPIO.HIGH)
        GPIO.output(motor2_pin2,GPIO.LOW)
def right():
        GPIO.output(motor1_pin1,GPIO.LOW)
        GPIO.output(motor1_pin2,GPIO.HIGH)
        GPIO.output(motor2_pin1,GPIO.LOW)
        GPIO.output(motor2_pin2,GPIO.LOW)
def stop():
        GPIO.output(motor1_pin1,GPIO.LOW)
        GPIO.output(motor1_pin2,GPIO.LOW)
        GPIO.output(motor2_pin1,GPIO.LOW)
        GPIO.output(motor2_pin2,GPIO.LOW)
forward()
time.sleep(3)
stop()