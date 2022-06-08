import yt_dlp

def download():
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