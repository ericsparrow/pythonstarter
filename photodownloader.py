import requests
import shutil
import mimetypes
from tkinter import *

root = Tk()

root.title("Photo Downloader by RICKY MONEY")
root.geometry('350x400')

lbl = Label(root, text = "Enter URL")
lbl.grid()

lbl2 = Label (root, text = "Enter file name")
lbl2.grid (column =0, row=1)

url = Entry(root, width=10)
url.grid(column =1, row=0)

file_name = Entry(root, width=10)
file_name.grid(column=1, row=1)

def clicked():

#url = input('Please enter an image URL (string):')
#file_name = input('Save image as (string):')

    try: 
        res = requests.get(url, stream = True)
        res.raise_for_status()

        content_type = res.headers.get('Content-Type', '')
        if 'image' in content_type:
            extension = mimetypes.guess_extension(content_type.split(';')[0])
            if not extension:
                extension = '.jpg'
        
            full_file_name = file_name + extension

            with open(full_file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)

            print('Image was successfully downloaded you fat bitch')
        else:
            print('The URL is wrong you dumb idiot')

    except requests.exceptions.RequestException as e:
        print('FAIL FAIL!! FAIL!!!')

btn = Button(root, text = "Enter" ,
        fg = "red", command=clicked)
btn.grid(column=2, row=3)

root.mainloop()