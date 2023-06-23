import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_folder_to_drive(folder_path, parent_folder_id=None):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    folder_name = os.path.basename(folder_path)
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    if parent_folder_id:
        folder_metadata['parents'] = [{'id': parent_folder_id}]

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_metadata = {'title': file_name, 'parents': [{'id': folder['id']}]}

            file = drive.CreateFile(file_metadata)
            file.SetContentFile(file_path)
            file.Upload()

            print(f"Uploaded: {file_name}")

        elif os.path.isdir(file_path):
            upload_folder_to_drive(file_path, folder['id'])

    print(f"Folder uploaded: {folder_name}")

# Specify the path of the folder containing the images
folder_path = 'example_folder'

# Call the function to upload the folder and its contents
upload_folder_to_drive(folder_path)

