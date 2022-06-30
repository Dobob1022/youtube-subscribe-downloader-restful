# youtube-subscribe-downloader-restful

## Welcome to the This Toy-Project!

Everything is using RESTful api.

Return Must be JSON!

### Used Library

Backend - Python(Flask),yt_dlp

Frontend - HTML+Bootstrap+Jquery

The app.py have internal threading fucntion.

When initializing web server, it will be start the download from DB!

### Add Link

The Channel and Playlist is available!

```
ENDPOINT : serverip:7000/db
{
  "link":"youtube_link"
}

If link is already in database

The Return will be
{
  "result": "duplicated"
}

With a BrandNew Link will be 
{
  "result": "OK"
}



```

### Load Link

Load Link From Database

Frontend -> query.html

``` json
Using Get Method to get Link List (Soon I will add auth fucntion.)
```



### FrontEnd with html+bootstrap+jquery

Still making....



