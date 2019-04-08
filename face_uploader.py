import os
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
        while True:
            path, dirs, files = next(os.walk("C:/Users/halda/OneDrive/Desktop/April/Faces"))
            file_count = len(files)
            for i in range(1,file_count+1):
                transferData.upload_file('Faces\\face'+str(i)+'.jpg','/face'+str(i)+'.jpg')
if __name__ == "__main__" :
    TransferData.main()
