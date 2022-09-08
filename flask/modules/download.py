import yt_dlp
import yt_dlp.utils

def download(download_links):
    for v0 in download_links:
        if 'playlist' in v0[1]:
            ydl_opt = {
            'outtmpl': './download/playlists/%(playlist_title)s/''%(title)s.%(ext)s',
            'format': 'best', #sel best qulity 
            'continue' : True,
            'verbose' : True,
            'no-overwrites' : True,
            'noplaylist' : True,
            'geo-bypass' : True,
            'ignoreerrors': True,
            'download_archive':'./download/archive.txt',
            }
            with yt_dlp.YoutubeDL(ydl_opt) as ydl:
                ydl.download(str(v0[1]))
        else:
            ydl_opt = {
            'outtmpl': './download/channels/%(channel)s/''%(title)s.%(ext)s',
            'format': 'best', #sel best qulity 
            'continue' : True,
            'verbose' : True,
            'no-overwrites' : True,
            'noplaylist' : True,
            'geo-bypass' : True,
            'ignoreerrors': True,
            'download_archive':'./download/archive.txt',
            }
            with yt_dlp.YoutubeDL(ydl_opt) as ydl:
                ydl.download(str(v0[1]))
    return({"msg":"Donwload Done!"})            
            
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
    except yt_dlp.utils.ExtractorError as e:
        return({
            "result":"fail",
            "code":"001"
        })

def only_download(link):
    ydl_opt = {
            'outtmpl': './download/playlists/%(playlist_title)s/''%(title)s.%(ext)s',
            'format': 'best', #sel best qulity 
            'continue' : True,
            'verbose' : True,
            'no-overwrites' : True,
            'noplaylist' : True,
            'geo-bypass' : True,
            'ignoreerrors': True,
            'download_archive':'./download/archive.txt',
            }
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download(link)