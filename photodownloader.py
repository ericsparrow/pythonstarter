import requests
import shutil
import mimetypes

url = input('Please enter an image URL (string):')
file_name = input('Save image as (string):')

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