import dropbox

class TransferData:
     def __init__(self, access_token):
        self.access_token = access_token

        
     def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'PnFwagtUqV8AAAAAAAAAAeRLn22lgS1lOvWXSave_rMZLGYWl5rZ23WvWr4jiyfn'
    transferData = TransferData(access_token)

    file_from = input("enter the path of the file you want to upload")

    file_to = input("enter the path of the dropbox")
  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
