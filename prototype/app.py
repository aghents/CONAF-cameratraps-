import tkinter as tk
from tkinter import filedialog
import os
import csv

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        print("Selected directory:", directory)
        # Process the selected directory with files

def browse_csv():
    csv_file = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"),))
    if csv_file:
        print("Selected CSV file:", csv_file)
        # Process the selected CSV file

def create_window():
    window = tk.Tk()
    window.title("File Uploader")

    directory_button = tk.Button(window, text="Upload Directory", command=browse_directory)
    directory_button.pack(pady=10)

    csv_button = tk.Button(window, text="Upload CSV", command=browse_csv)
    csv_button.pack(pady=10)

    window.mainloop()

# Run the application
create_window()