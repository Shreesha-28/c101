import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.ArZPgYzaJT65RFdMJQhoxfIH2Qlqgeo24ZHBZJ9llL97-mpOOsVFWRJSZYKqgs7LxtX698xb-TOqDHQOSJR_4K6K-JPLo60dldk4USuSQYNt7bZuc22l7Nc7_iI2KNKNPvN-OxU'
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer: ")
    file_to=input("enter the fullpath to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("file has been moved successfully")

main()