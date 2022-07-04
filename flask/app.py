from flask import Flask,request, Response
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
    videoInfo = bs(url_opener, features="html.parser")
    video_title = videoInfo.title.get_text()
    return video_title

## route area
@app.route('/')
def main():
    return Response(status=405)

@app.route('/api/db', methods = ['GET','POST','DELETE']) 
def dbjob():
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
        print(params)
        if not request.is_json: #is json format?
            return ({"msg": "Missing JSON in request"})
        else:
            #link check
            request_url = params['link']
            if youtube_url_validation(request_url) != True or link_avaliablity(request_url) !=  True: #404 or youtube link validation
                return ({"msg":"Invaild_Youtube_Link"})
                #404 check
            name = get_channel_name(request_url)
            return db.insert_link(request_url, name),200
            
    ## Delate Link Function
    elif request.method=="DELETE":
        params = request.get_json()
        if not request.is_json:
            return ({"msg": "Missing JSON in request"})
        else:
            idList = json.loads(json.dumps(params))
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
        password = request.form.get("password")
        dbpassword = db.load_password()[0][0] 
        if (bcrypt.checkpw(password.encode('UTF-8'),dbpassword.encode('UTF-8'))) == False:
            # password incorrect
            return "Password incorrect"
        elif (bcrypt.checkpw(password.encode('UTF-8'),dbpassword.encode('UTF-8'))) == True:
            # password correct!
            return "SUCESS!"
        else:
            return "Something is Wrong"
    else:
        return Response(status=405)
@app.route('/api/password', methods=['PUT'])
def changepw():
    if request.method == "PUT":
        pass
        #password update fucntion reqired


@app.route('/api/update')
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

if __name__ == "__main__":
    # threading.Thread(target = thread_download).start()
    app.run(debug=True, host = '0.0.0.0',port=7000)
    
    
    
