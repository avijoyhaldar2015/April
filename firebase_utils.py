import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from random import randint
# Fetch the service account key JSON file contents
cred = credentials.Certificate('C://XXXX/april-XXXXXXXXXXXXX-firebase-adminsdk-XXXXX-XXXXXXXXXX.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://april-XXXXXXXXXXXXX.firebaseio.com/'
})
def voice_authentication():   
    print("Waiting for Voice Authentication...")
    r=db.reference('/April/').update({'message' : 'xxxxxx'})
    r=db.reference('/April/').update({'otp' : 'xxxx'})
    var_x=0
    while(True):
        ref = db.reference('April')
        res = ref.get()
        if(str(res['message'])=="\"6380 180 308\"" and var_x==0):
            print("Voice Authentication Successful!")
            var_x=1
            otp=randint(1000,9999)
            otp_db=db.reference('/April/').update({'otp' : str(otp)})
            otp_checker=input('Enter the secure code:')
            if(otp_checker==str(otp)):
                print('Login Successful!')
                break
def geolocation():
    ref = db.reference('April')
    res = ref.get()
    print('Getting Device Location Details...')
    return res['lat'],res['lng']
def obstacleflag():
    ref = db.reference('April')
    res = ref.get()
    return res['obstacle_flag']
def ground_bot_connection_validation(value):
    ref = db.reference('/April/').update({'bot_uplink' : '+1'})
    ref2= db.reference('April')
    res = ref2.get()
    if(res['bot_downlink']=='+1'):
        return True
    else:
        return False
def close_ground_bot_connection():
    ref=db.reference('/April/').update({'bot_uplink' : '0'})
def get_destination_latitude():
    ref=db.reference('April')
    res=ref.get()
    return res['dest_lat']
def get_destination_longitude():
    ref=db.reference('April')
    res=ref.get()
    return res['dest_lng']
def rpicommtransmitter( direction, value ):
    if(direction=='forward'):
        ref = db.reference('/April/').update({'motor_1' : '+1'})
        ref = db.reference('/April/').update({'motor_2' : '+1'})
        ref = db.reference('/April/').update({'value_1' : '+1'})
        ref = db.reference('/April/').update({'value_2' : '+1'})
    elif(direction=='backward'):
        ref = db.reference('/April/').update({'motor_1' : '-1'})
        ref = db.reference('/April/').update({'motor_2' : '-1'})
        ref = db.reference('/April/').update({'value_1' : '+1'})
        ref = db.reference('/April/').update({'value_2' : '+1'})
    elif(direction=='left'):
        ref = db.reference('/April/').update({'motor_1' : '-1'})
        ref = db.reference('/April/').update({'motor_2' : '+1'})
        ref = db.reference('/April/').update({'value_1' : '50'})#Assuming that 50 ticks + and - makes the bot turn 90 degrees in its position.
        ref = db.reference('/April/').update({'value_2' : '50'})
        ref = db.reference('/April/').update({'motor_1' : '+1'})
        ref = db.reference('/April/').update({'motor_2' : '+1'})
        ref = db.reference('/April/').update({'value_1' : '+1'})
        ref = db.reference('/April/').update({'value_2' : '+1'})
    elif(direction=='right'):
        ref = db.reference('/April/').update({'motor_1' : '+1'})
        ref = db.reference('/April/').update({'motor_2' : '-1'})
        ref = db.reference('/April/').update({'value_1' : '50'})#Assuming that 50 ticks + and - makes the bot turn 90 degrees in its position.
        ref = db.reference('/April/').update({'value_2' : '50'})
        ref = db.reference('/April/').update({'motor_1' : '+1'})
        ref = db.reference('/April/').update({'motor_2' : '+1'})
        ref = db.reference('/April/').update({'value_1' : '+1'})
        ref = db.reference('/April/').update({'value_2' : '+1'})
    elif(direction=='rotate clockwise'):
        ref = db.reference('/April/').update({'motor_1' : '+1'})
        ref = db.reference('/April/').update({'motor_2' : '-1'})
        ref = db.reference('/April/').update({'value_1' : value})
        ref = db.reference('/April/').update({'value_2' : value})
    elif(direction=='rotate anticlockwise'):
        ref = db.reference('/April/').update({'motor_1' : '-1'})
        ref = db.reference('/April/').update({'motor_2' : '+1'})
        ref = db.reference('/April/').update({'value_1' : value})#Assuming that 50 ticks + and - makes the bot turn 90 degrees in its position.
        ref = db.reference('/April/').update({'value_2' : value})
    elif(direction=='stop'):
        ref = db.reference('/April/').update({'motor_1' : '0'})
        ref = db.reference('/April/').update({'motor_2' : '0'})
        ref = db.reference('/April/').update({'value_1' : '+1'})
        ref = db.reference('/April/').update({'value_2' : '+1'})
