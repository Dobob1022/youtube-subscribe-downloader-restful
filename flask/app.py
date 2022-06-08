from flask import Flask, render_template, request, flash, redirect, session
from modules
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods = ['GET','POST'])
def main():
    if request.method=="GET":
        return "METHOD NOT ALLOWED!"
    if request.method=="POST":
        return "METHOD NOT ALLOWED!"

@app.route('/readdb', methods = ['GET'])
def readdb():
    if request.method=="GET":
        #readDB Function Required
        return "READDB"
    else:
        return "METHOD NOT ALLOWED!"
@app.route('/download', method = ['GET'])
def download():
    if request.method=="GET":
        #yt-dlp download require
        return "DOWNLOAD COMPLETE"
    else:
        return "METHOD NOT ALLOWED!"

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
 