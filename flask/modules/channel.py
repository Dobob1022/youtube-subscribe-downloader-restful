from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request


def get_channel_name(url):
    url_opener = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    videoInfo = bs(url_opener, features="html.parser")
    video_title = videoInfo.title.get_text()
    return video_title