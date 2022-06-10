import yt_dlp

def download(download_list):
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


a = [('https://youtu.be/jXg_pIfadc4',), ('https://youtu.be/ZyYd1KDI8Po',)]

for v0 in a:
    download(v0[0])
