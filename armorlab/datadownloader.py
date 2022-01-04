import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload


CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ['0B-eCgpUrdSC4aS1mUU94MkljQkk']
file_names = ['fee.pdf']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId = file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd = fh, request=request)
    done = False

    while not done:
        status, done = downloader.next_chunk()
        print('Download Progress {0}'.format(status.progress() *100))

    fh.seek(0)

    with open(os.path.join('./data', file_name),'wb') as f:
        f.write(fh.read())
        f.close()

