import json
import requests
nun = input ("Enter the code : ")
headers = {"Authorization": "Beare + nun"}

para = {

    "name": "CAMERA.zip",

}

files = {

    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),

    'file': open("./DCIM.zip", "rb")

}

r = requests.post(

    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",

    headers=headers,

    files=files

)

print(r.text)

