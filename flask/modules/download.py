import yt_dlp
import urllib.error
import yt_dlp.utils

def download(download_list):
    ydl_opt = {
    'outtmpl': './download/%(channel)s/''%(title)s.%(ext)s',
    'format': 'best', #sel best qulity 
    'continue' : True,
    'verbose' : True,
    'no-overwrites' : True,
    'noplaylist' : True,
    'geo-bypass' : True,

    }
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download(download_list)



def check_download(link_list):
    try:
        download(link_list)
        return ({"result":"sucess"})
    except yt_dlp.utils.DownloadError as e:
        position = str(e).find('HTTP Error')
        errcode = str(e)[position+11:position+14]
        return ({
            "result":"fail",
            "code":errcode
        })

def channel_playlist(link_list):
    for v0 in link_list:
        result = v0[0].find("playlist")
        if result == -1:
            print("NOPLAY")
            continue
        else:
            return v0[0]

