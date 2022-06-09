from flask import Flask, render_template, request, flash, redirect, session, Response,jsonify
from modules import db
import os
import json
import re
import ast



app = Flask(__name__)
app.secret_key = os.urandom(32)

## function area
import re

def youtube_url_validation(url):
    regex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
    youtube_regex_match = re.match(regex, url)
    if youtube_regex_match:
        return True

    return False



## route area
@app.route('/', methods = ['GET','POST'])
def main():
    if request.method=="GET":
        return Response(status=405)
    if request.method=="POST":
        return Response(status=405)

@app.route('/db', methods = ['GET','POST','PUT'])
def readdb():
    if request.method=="GET":
        #readDB Function Required
        return "READDB"
    elif request.method=="PUT":
        print(request.is_json)
        params = request.get_json()
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            #link check
            request_url = params['link']
            if youtube_url_validation(request_url) == True:
                pass
            else:
                return jsonify({"msg":"Invaild_Youtube_Link"}),400
            #db insert
            return jsonify({"req":params['link']})
            # return jsonify({"msg": "OK"}), 200
        
    else:
        return Response(status=405)


# @app.route('/download', method = ['POST'])
# def download():
#     if request.method == "GET":
#         #yt-dlp download require
#         return "DOWNLOAD COMPLETE"
#     else:
#         return Response(status=405)


#Response({"a":"b"}, status=201, mimetype='application/json)
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
 