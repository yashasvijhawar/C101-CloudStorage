import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                localPath = os.path.join(root,fileName)
                relativePath = os.path.relpath(localPath,file_from)
                dropboxPath = os.path.join(file_to,relativePath)
                with open(localPath,'rb')as f:
                    dbx.files_upload(f.read(),dropboxPath,mode = WriteMode('overwrite'))
        #with open(file_from,'rb') as f:
            #dbx.files_upload(f.read(),file_to)

def main():
        access_token = 'sl.AyXieUkoF_jIE4QtdyQT0NoV2c8w9p5RMKws6aM9bkaJlfU4EYywhpvkzq2oTtVhIRZZXqrf2LUmKaevALNEDmqbsUAG07s03zj7PbGmGuFJl9C4pgxrIk7_xhLofy6BFJQl0SE'
        transferData = TransferData(access_token)

        file_from = str(input("Enter the folder path to transfer"))
        file_to = input("Enter the full path to upload to dropbox")

        transferData.upload_file(file_from,file_to)
        print("file has been moved")

main()