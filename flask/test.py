# import re

# def youtube_url_validation(url):
#     regex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
#     youtube_regex_match = re.match(regex, url)
#     if youtube_regex_match:
#         return youtube_regex_match

#     return youtube_regex_match

# print(youtube_url_validation("https://youtube.com/channel/123"))




import yt_dlp
    





from modules import db
import json

getdata = db.load_link()

result = []



for v0 in getdata:
    result.append(v0[0])
    print(v0[0])

print("RESULT:",result)

really = json.dumps(result)

print(really)

cyka = json.loads(really)

print(cyka[0])


def download(link):
    download_list = [link,
    ]

    ydl_opt = {
    'outtmpl': './download/%(channel)s/''%(title)s.%(ext)s',
    'format': 'best', #sel best qulity 
    'continue' : True,
    'verbose' : True,
    'no-overwrites' : True,
    'noplaylist' : True,  
    }
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download(download_list)

for v0 in cyka:
    download(v0)
