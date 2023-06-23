import os
import tkinter as tk
from tkinter import filedialog
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import csv
from pymongo import MongoClient

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
    return folder_name

def upload_files_to_drive(directory_path):
    folder_name = upload_folder_to_drive(directory_path)
    info_label.config(text=f"Authentication successful.\nFolder uploaded: {folder_name}")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        print("Selected directory:", directory)
        upload_files_to_drive(directory)

def browse_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        print("Selected CSV file:", file_path)
        # MongoDB connection URI
        uri = "mongodb+srv://agustinsso:1234@cluster0.tbwegic.mongodb.net/?retryWrites=true&w=majority"

        # Name of the target database and collection
        database_name = "conaf_reports"
        collection_name = "reports"

        # Path to the CSV file
        csv_file_path = "csv.csv"

        # Create a new client and connect to the MongoDB server
        client = MongoClient(uri)

        # Access the target database and collection
        db = client[database_name]
        collection = db[collection_name]

        # Read the CSV file and insert its contents into the collection
        with open(csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            collection.insert_many(data)

        # Close the MongoDB connection
        client.close()

def create_window():
    window = tk.Tk()
    window.title("File Uploader")

    directory_button = tk.Button(window, text="Upload Directory", command=browse_directory)
    directory_button.pack(pady=10)

    csv_button = tk.Button(window, text="Upload CSV File", command=browse_csv_file)
    csv_button.pack(pady=10)

    global info_label
    info_label = tk.Label(window, text="")
    info_label.pack(pady=10)

    window.mainloop()

# Run the application
create_window()
