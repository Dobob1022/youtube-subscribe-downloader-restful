from typing import final
from flask import Flask,request, Response,jsonify
from modules import db, download
import os
import re
import json
import requests
import threading
import time
import re
import bcrypt
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import ast
#CORS
from flask_cors import CORS

#flaskthing
app = Flask(__name__)
app.secret_key = os.urandom(32)
CORS(app) # CORS

## function area


def youtube_url_validation(url):
    regex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
    youtube_regex_match = re.match(regex, url)
    if youtube_regex_match:
        return True
    return False

def link_avaliablity(url):
    request = requests.get(url)
    if str(request).find("404") == -1: # if find function return -1 -> there is no 404 code
        return True
    return False

def get_channel_name(url):
    url_opener = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    videoInfo = bs(url_opener, features="html.parser") # bull shit
    video_title = videoInfo.title.get_text()
    return video_title

## route area
@app.route('/')
def main():
    return Response(status=405)

@app.route('/db', methods = ['GET','POST']) 
def dbjob():
    if request.method=="GET":
        result = []
        for dataList in db.load_link():
            result.append({
                'ChannelUrl': dataList[0],
                'ChannelTitle': dataList[1]
            })
        return json.dumps(result)
    elif request.method=="POST":
        params = request.get_json()
        if not request.is_json: #is json format?
            return ({"msg": "Missing JSON in request"})
        else:
            #link check
            request_url = params['link']
            # print(request_url) 말그대로 url
            if youtube_url_validation(request_url) != True or link_avaliablity(request_url) !=  True: #404 or youtube link validation
                return ({"msg":"Invaild_Youtube_Link"})
                #404 check
            name = get_channel_name(request_url)
            return db.insert_link(request_url, name),200
    else:
        return Response(status=405)


@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return Response(status=405)
    elif request.method == "POST":
        password = request.form.get("password")
        dbpassword = db.load_password()[0][0] 
        if (bcrypt.checkpw(password.encode('UTF-8'),dbpassword.encode('UTF-8'))) == False:
            # password incorrect
            return "Password incorrect"
        elif (bcrypt.checkpw(password.encode('UTF-8'),dbpassword.encode('UTF-8'))) == True:
            # password correct!
            return "SUCESS!"
        else:
            return "Something is worng"
    else:
        return Response(status=405)
@app.route('/password', methods=['PUT'])
def changepw():
    if request.method == "PUT":
        pass
        #password update fucntion reqired


@app.route('/update', methods = ['GET','POST','PUT'])
def ytdlp_update():
    try:
        os.system("pip install -U yt-dlp")
        return({"result":"sucess"})
    except:
        return({"result":"failed"})



def thread_download():
    while True:
        getdata = db.load_link()
        print(download.check_download(getdata))
        time.sleep(7200)

#Response({"a":"b"}, status=201, mimetype='application/json
if __name__ == "__main__":
    # threading.Thread(target = thread_download).start()
    app.run(debug=True, host = '0.0.0.0',port=7000)
    
    
    
