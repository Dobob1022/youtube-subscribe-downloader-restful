from urllib import response
from flask import Flask, redirect,request, Response, session
from modules import db, download
import os
import re
import json
import requests
import threading
import time
import re
import bcrypt
import jwt
import jwt.exceptions
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
#CORS
from flask_cors import CORS

#flask_thing
application = app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app) # CORS

## function area

def jwtVerify(token):
    try:
        decode = jwt.decode(token.replace("Bearer ", ""), "yee yee ass hair cut", algorithms="HS256") 
        print(decode)
        if decode['login'] == "true":
            return True
    except jwt.exceptions.DecodeError as e:
        return False
    except AttributeError as e:
        return False

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
    try:
        url_opener = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    except:
        False
    else:
        videoInfo = bs(url_opener, features="html.parser")
    try:
        video_title = videoInfo.title.get_text()
    except:
        return False
    else:
        return video_title

## route area
@app.route('/')
def main():
    return Response(status=405)

@app.route('/api/db', methods = ['GET','POST','DELETE']) 
def dbjob():
    if jwtVerify(request.headers.get('Authorization')) == False:
        return ({"msg":"Not Logined"}),401
## Query Link Fucntion
    if request.method=="GET":
        result = []
        for dataList in db.load_link():
            result.append({
                'id':dataList[0],
                'Title': dataList[2],
                'URL': dataList[1]
            })
        # return json format result
        if result == []:
            return ({"msg":"List is Empty"}),500
        return json.dumps(result)

    ## Insert Link Fucntion
    elif request.method=="POST":
        params = request.get_json()
        if not request.is_json: #is json format?
            return ({"msg": "Missing JSON in request"})
        else:
            #link check
            request_url = params['link']
            if youtube_url_validation(request_url) != True or link_avaliablity(request_url) !=  True: #404 or youtube link validation
                return ({"msg":"Invaild Youtube Link"})
                #404 check
            name = get_channel_name(request_url)
            #issue #6
            if name == False:
                return ({"msg":"Channel Or Playlist is unavailable."})
            result = db.insert_link(request_url, name),200
            #issue #08
            download.only_download(request_url)
            return result
            
    ## Delate Link Function
    elif request.method=="DELETE":
        params = request.get_json()
        print(params)
        if not request.is_json:
            return ({"msg": "Missing JSON in request"})
        else:
            idList = json.loads(json.dumps(params)) #get json from frontend and serialize
            ids = []
            for v0 in idList:
                ids.append(int(v0['id']))
            return db.delete_link(ids)


    #wrong method execption
    else:
        return Response(status=405)


@app.route('/api/login', methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return Response(status=405)
    elif request.method == "POST":
        password = request.get_json()['password']
        if password == "":
            return ({"msg":"Password must be not empty!"})
        dbpassword = db.load_password()[0][0] 
        if (bcrypt.checkpw(password.encode('UTF-8'),dbpassword.encode('UTF-8'))) == False:
            # password incorrect
            return ({"msg":"Password incorrect"}),401
        elif (bcrypt.checkpw(password.encode('UTF-8'),dbpassword.encode('UTF-8'))) == True:
            # password correct!
            accessToken = jwt.encode({"login":"true"}, "yee yee ass hair cut",algorithm="HS256")
            return ({"msg": accessToken })
        else:
            return {"msg":"Something is Wrong"}
    else:
        return {"msg":"Something is Wrong"}

@app.route('/api/password', methods=['PUT'])
def changepw():
    if jwtVerify(request.headers.get('Authorization')) == False:
        return ({"msg":"Not Logined"}),401
    if request.method == "PUT":
        new_password = request.get_json()['password']
        new_password = new_password.encode('UTF-8')
        new_password= bcrypt.hashpw(new_password,bcrypt.gensalt()).decode('UTF-8')
        return db.change_pw(new_password)

@app.route('/api/update', methods=["POST"])
def ytdlp_update():
    if jwtVerify(request.headers.get('Authorization')) == False:
        return ({"msg":"Not Logined"}),401
    if request.method == "POST":
        try:
            os.system("pip install -U yt-dlp")
            return({"msg":"Success!"})
        except:
            return({"msg":"Update Failed"})
    else:
        return ({"msg":"Method Not Allowed"}),405

@app.route('/api/download',methods=["POST"])
def DownloadNow():
    getdata = db.load_link()
    return(download.download(getdata))




    


def download_thread():
    while True:
        getdata = db.load_link()
        download.check_download(getdata)
        time.sleep(7200)
def start_thread():
    t = threading.Thread(target = download_thread)
    t.daemon = True
    t.start()


if __name__ == "__main__":
    start_thread()
    app.run(host = '0.0.0.0',port=7000)
    
    
    
    
