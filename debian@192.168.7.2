import cv2
import sys
import dropbox
import time
import http.client
import socket
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def download_file(self,file_to_download,file_to_save):
        dbx=dropbox.Dropbox(self.access_token)
        f,ms=dbx.file_download(file_to_download)
        string=str(ms.content)
        ans=string
        stat_file=open(file_to_save,"w")
        stat_file.write(ans)
        stat_file.close()
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            overwrite=True
            try:
                mode=(dropbox.files.WriteMode.overwrite
                if overwrite
                else dropbox.files.WriteMode.add)
                dbx.files_upload(f.read(), file_to, mode)
            except dropbox.exceptions.ApiError as err:
                print("API Error ",err)
    def check_device_internet_connection(self):
        test_conn_url="www.google.com"
        test_con_resource="/intl/en/policies/privacy/"
        test_con=http.client.HTTPConnection(test_conn_url)
        try:
            test_con.request("GET",test_con_resource)
        except http.client.ResponseNotReady as e:
            return 0
        except socket.gaierror as e:
            return 0
        else:
            return 1
    def text_to_json(text_data):
        json=demjson.encode(text_data)
    def main():
        access_token = 'i83r5cO1h-AAAAAAAAAAQRZGFetI7LGV1UITXAIG_Jabwgzodm7-2q-9lAAkWY3f'
        transferData=TransferData(access_token)
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_capture = cv2.VideoCapture(0)
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            znn=0
            face_counter=0
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (znn, 255, 0), 2)
                znn=znn+1
                if znn!=0:
                    face_counter=face_counter+1
                cv2.imwrite('Frames\\frame.jpg',frame)
                img=cv2.imread('Frames\\frame.jpg')
                crop_img=img[y:y+h, x:x+h]
                cv2.imwrite('Faces\\face'+str(face_counter)+'.jpg', crop_img)
                
                if face_counter>0:
                    for i in range(1,face_counter+1):
                        transferData.upload_file('Faces\\face'+str(i)+'.jpg','/face'+str(i)+'.jpg')
                #exit()
            # Display the resulting frame
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    TransferData.main()    
