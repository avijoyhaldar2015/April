import firebase_utils
import face_detection
import subprocess
import os
#import AES
def main():
    print("Welcome to April Defense Systems v1.0 Beta!")
    firebase_utils.close_ground_bot_connection()
    while(True):
        command=input(">>>")
        if(command=="start mission"):
            print("Initiating Voice Authentication...")
            firebase_utils.voice_authentication()
            print("Authentication Procedure Successful!")
            x=input("Do you want to commence mission?[y/n]:")
            if(x=="y"):
                print("Mission Started...")
                x_1,y_1=firebase_utils.geolocation()
                print('GPS Position aquired!')
                print(x_1)
                print(y_1)
                while(firebase_utils.get_destination_latitude()==0 and firebase_utils.get_destination_longitude()==0):
                    print('Getting destination co-ordinates...')
                print('Destination Set!')
                print(firebase_utils.get_destination_latitude())
                print(firebase_utils.get_destination_longitude())
                print('Mission underway...')
        elif(command=="run system diagnostics"):
            print('System Diagnostics Running...')
            while(True):
                diag_comm=input('/System_Diagnostics/>>>')
                if(diag_comm=="cvs"):
                    print('Running Vision Systems...')
                    face_detection.TransferData.main()
                elif(diag_comm=="check encryption"):
                    file_name=input('Enter File to be encrypted:')
                    #AES.encrypt_file(file_name)
                elif(diag_comm=="check bot control"):
                    while(True):
                        if(firebase_utils.ground_bot_connection_validation('+1')==True):
                            print('Connection to Bot Established...')
                            break
                        else:
                            print('Connection to Bot Failed... Please retry!')
                    while(True):
                        xcomm=input('/System_Diagnostics/Botcomm/>>>')
                        if(xcomm=='w'):
                            firebase_utils.rpicommtransmitter('forward','122')
                        elif(xcomm=='x'):
                            firebase_utils.rpicommtransmitter('stop','233')
                        elif(xcomm=='z'):
                            print('Terminating Connection to Bot...')
                            firebase_utils.close_ground_bot_connection()


if __name__=="__main__":
    main()
