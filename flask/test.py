# import re

# def youtube_url_validation(url):
#     regex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
#     youtube_regex_match = re.match(regex, url)
#     if youtube_regex_match:
#         return youtube_regex_match

#     return youtube_regex_match

# print(youtube_url_validation("https://youtube.com/channel/123"))


# from modules import db
# import json

# getdata = db.load_link()

# result = []



# for v0 in getdata:
#     result.append(v0[0])
#     print(v0[0])

# print("RESULT:",result)

# really = json.dumps(result)

# print(really)

# cyka = json.loads(really)

# print(cyka[0])


# def download(link):
#     download_list = [link,
#     ]

#     ydl_opt = {
#     'outtmpl': './download/%(channel)s/''%(title)s.%(ext)s',
#     'format': 'best', #sel best qulity 
#     'continue' : True,
#     'verbose' : True,
#     'no-overwrites' : True,
#     'noplaylist' : True,  
#     }
#     with yt_dlp.YoutubeDL(ydl_opt) as ydl:
#         ydl.download(download_list)

# for v0 in cyka:
#     download(v0)


# from modules import download, db

# print(download.check_download("https://www.youtube.com/playlist?list=PL9aQlZr3wxbiaAv5aD-FRXArcCrXzDcwz"))


# a ="ERROR: [generic] Unable to download webpage: HTTP Error 401: Unauthorized (caused by <HTTPError 401: 'Unauthorized'>); please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U"
# b = a.find('HTTP Error')
# print(a[b+11:b+14])


##check require
# from modules import db, download

# db.insert_link("https://www.youtube.com/playlist?list=PL9aQlZr3wxbiaAv5aD-FRXArcCrXzDcwz")
# db.insert_link("https://www.youtube.com/channel/UCUkZCwVhUvoYWaTkujQJZ0Q")

# a = db.load_link()



# b = download.channel_playlist(a)


# print(a)

## 404 Validataion
# import re
# import requests
# from modules import db
# def youtube_url_validation(url):
#     regex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
#     youtube_regex_match = re.match(regex, url)
#     if youtube_regex_match:
#         return True
#     return False

# def link_avaliablity(url):
#     request = requests.get(url)
#     print(str(request))
#     if str(request).find("404") == -1:
#         pass
#     else:
#         return 404
#     return request

# from modules import download, db

# list = db.load_link()



# download.download(a)


# from modules import download, db

# download.only_download("https://youtu.be/RzZ3STEI35s")


# import jwt

# token = jwt.encode({"password":"dobob"},"SECRET",algorithm="HS256")

# print(token)

# import bcryp
# from modules import db

# password = "defaultpassword".encode('UTF-8')

# db_pw = db.load_password()
# db_pw = db_pw[0][0]

# db_pw = db_pw.encode('UTF-8')


# print(bcrypt.checkpw(password,db_pw))
# import json
# import yt_dlp

# URL = 'https://www.youtube.com/channel/UCUkZCwVhUvoYWaTkujQJZ0Q'

# # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
# ydl_opts = {}
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(URL, download=False)

#     # ℹ️ ydl.sanitize_info makes the info json-serializable
#     channel_name=json.dumps(ydl.sanitize_info(info))
#     json_data = json.loads(channel_name)
#     print(channel_name['uploader'])

# a = "https://www.youtube.com/channel/UCLJNGmEfcuugzEjLyZ6mKKw"
# # b = "도밥이"
# # for v0,v1 in zip(str(a),str(b)):
# #     print(a,b)

# from modules import db
# b = db.delete_link(a)
# print(b)

# import jwt

# accessToken = jwt.encode({"":""}, "yee yee ass hair cut",algorithm="HS256")
# print(accessToken)
# decode = jwt.decode(accessToken, "yee yee ass hair cut", algorithms="HS256")
# print(decode)

# if decode[''] == '':
#     print("fuckyou")
# else:
#     print("DICK")









# import requests
# import json
# import jwt
# authpassword = {'password':'defaultpassword'}
# headers = {'Content-Type': 'application/json; charset=utf-8'}
# def get_jwt():
#         response = requests.post('http://127.0.0.1:7000/api/login', headers=headers ,data=json.dumps(authpassword))
#         print(response)
#         authinfo = json.loads(response.text)
#         return authinfo['msg']

# print(get_jwt())

# def jwtVerify(token):
#     try:
#         decode = jwt.decode(token.replace("Bearer ", ""), "yee yee ass hair cut", algorithms="HS256") 
#         print(decode)
#         if decode['login'] == "true":
#             return True
#     except jwt.exceptions.DecodeError as e:
#         return False
#     except AttributeError as e:
#         return False

# print(jwtVerify(get_jwt()))

# import json
# import requests


# output = requests.get("http://127.0.0.1:7000/api/db", headers=header)

# json_load = json.loads(requests.get("http://127.0.0.1:7000/api/db", headers=header).text)
# # print(json.dumps(output))

# # b = json.loads(output.text)

# print(json_load[-1]['id'])



# # print(b[-1]['id'])

import json
import requests

header={
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRydWUifQ.ujrl2ZZPJWit0WywQRUGfWkgcOndYgznNFQdd9pj1Lg"
            }


jsonLoad = json.loads(requests.get("http://127.0.0.1:7000/api/db", headers=header).text)
number = jsonLoad[-1]['id']
req = {"id":f"{number}"}
print([json.dumps(req)])
response = requests.delete("http://127.0.0.1:7000/api/db", headers=header,data=json.dumps([req]))

print(response)


