from flask import Flask,request, Response,jsonify
from modules import db, download
import os
import re
import json
import requests
import threading
import time
import re

app = Flask(__name__)
app.secret_key = os.urandom(32)

## function area


def youtube_url_validation(url):
    regex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
    youtube_regex_match = re.match(regex, url)
    if youtube_regex_match:
        return True
    return False

def link_avaliablity(url):
    request = requests.get(url)
    print(str(request))
    if str(request).find("404") == -1:
        pass
    else:
        return ({"result":"404"})
    return True

## route area
@app.route('/')
def main():
    return Response(status=405)

@app.route('/db', methods = ['GET','POST'])
def dbjob():
    if request.method=="GET":
        #readDB Function Required
        getdata = db.load_link()
        result = []
        for v0 in getdata:
            result.append(v0[0])
            print(v0[0])
        jsonoutput = json.dumps(result)
        return jsonoutput


    elif request.method=="POST":
        print(request.is_json)
        params = request.get_json()
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            #link check
            request_url = params['link']
            if youtube_url_validation(request_url) == True:
                #404 check
                if link_avaliablity(request_url) ==  True:
                    #DB INSERT
                    return db.insert_link(params['link']),200
                else:
                    return jsonify({"msg":"Invaild_Youtube_Link"}),400
            else:
                return jsonify({"msg":"Invaild_Youtube_Link"}),400

            # return jsonify({"msg": "OK"}), 200
        
    else:
        return Response(status=405)


@app.route('/login', methods = ['GET','POST'])
def changepw():
    if request.method == "GET":
        return Response(status=405)

    elif request.method == "POST":
        password = request.form.get("password")
        print(password)
        return password
    else:
        return Response(status=405)


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
    app.run(debug=True, host = '0.0.0.0')
    
    
    
