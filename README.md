# youtube-subscribe-downloader-restful

## Welcome to the This Toy-Project!

Everything is using RESTful api.

Return Must be JSON!

### Used Library

Python(Flask),yt_dlp

The app.py have internal threading fucntion.

When initializing web server, it will be start the download from DB!

### Add Link

The Channel and Playlist is available!

```json

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

``` json
Using Get Method to get Link List
```

