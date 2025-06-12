import requests
import shutil
import mimetypes
from tkinter import *
from tkinter import filedialog
import os

root = Tk()

folder_var = StringVar()

def browse_folder():
    global selected_folder
    foldername = filedialog.askdirectory()
    if foldername:
        folder_var.set(foldername)

root.title("Photo Downloader by RICKY MONEY")
root.geometry('400x100')

browse_button = Button(root, text="Select Folder...", command=browse_folder)
browse_button.pack(pady=20)
browse_button.grid (column =2, row=3)

destfolder = Label(root, text = "Destination")
destfolder.grid(column=0, row=3)

displayfolder = Entry(root, textvariable=folder_var, width=30)
displayfolder.grid(column=1, row=3)

lbl = Label(root, text = "Enter URL")
lbl.grid(column =0, row =0)

lbl2 = Label (root, text = "Enter file name")
lbl2.grid (column =0, row=1)

url = Entry(root, width=30)
url.grid(column =1, row=0)

file_name = Entry(root, width=30)
file_name.grid(column=1, row=1)

def clicked():
    global file_extension
    input_url = url.get()
    input_file_name = file_name.get()

    try:
        res = requests.get(input_url, stream=True)
        res.raise_for_status()

        content_type = res.headers.get('Content-Type', '')
        if 'image' in content_type:
            extension = mimetypes.guess_extension(content_type.split(';')[0])
            file_extension = extension
            if not extension:
                extension = '.jpg'

            full_file_name = input_file_name + extension

            with open(full_file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)

            print('Image was successfully downloaded.')
        else:
            print('The URL does not appear to be an image.')
    except requests.exceptions.RequestException as e:
        print(f'FAIL FAIL FAIL: {e}')

file_extension = ""

full_file_path = os.path.join(folder_var, file_name + file_extension)

btn = Button(root, text = "Enter" ,
        fg = "red", command=clicked)
btn.grid(column=2, row=4)

root.mainloop()