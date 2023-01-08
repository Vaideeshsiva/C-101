import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.BWgEgNfVoyMg-LJrSjYnGGlH47WST-hTbu9-5zx2Z7FIF1FAbGVTJNyQbZ3bEh1ELIt7CQUFpXEkqXjQIR9JjLz6fEEJhGHzSzkeOP9mGfY3xrlEKQdHHLbEOgK2Fd4L9X96P58'
    transferData = TransferData(access_token)

    file_from = input("Enter file path to transfer: ")
    file_to = input("Enter full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved!")

if __name__ == 'main':
    main()