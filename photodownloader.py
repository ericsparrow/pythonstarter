import requests
import shutil
import mimetypes
from tkinter import *

root = Tk()

root.title("Photo Downloader by RICKY MONEY")
root.geometry('400x100')

lbl = Label(root, text = "Enter URL")
lbl.grid()

lbl2 = Label (root, text = "Enter file name")
lbl2.grid (column =0, row=1)

url = Entry(root, width=30)
url.grid(column =1, row=0)

file_name = Entry(root, width=30)
file_name.grid(column=1, row=1)

def clicked():
    input_url = url.get()
    input_file_name = file_name.get()

    try:
        res = requests.get(input_url, stream=True)
        res.raise_for_status()

        content_type = res.headers.get('Content-Type', '')
        if 'image' in content_type:
            extension = mimetypes.guess_extension(content_type.split(';')[0])
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

btn = Button(root, text = "Enter" ,
        fg = "red", command=clicked)
btn.grid(column=2, row=3)

root.mainloop()