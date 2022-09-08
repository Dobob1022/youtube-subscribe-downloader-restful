# youtube-subscribe-downloader-restful

## Welcome to the This Toy-Project!

Every communication will use RESTful API and JSON!

### Used Library

Backend - Python(Flask),yt_dlp,ETC...

Frontend - HTML+Bootstrap+Jquery

## docker location

in docker-compose.yml

you can see the 
```
volumes:
            - "HostPath:/app/download" #download folder
            - "HostPath:/app/db" #db backup
```
You need to Change HostPath Location in host location

### Add Link

The Channel and Playlist is available!

```
EndPoint : ServerIP:Port/api/db
Method : "POST"

The Format must be like this ->
{
  "link":"youtube_link(Channel, Playlist)"
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

### Delete Link

```
EndPoint : ServerIP:Port/api/db
Method : "DELETE"


requst type must be like this
{
	"link":"delete_youtube_link"
}

If the remove from db is sucessfully. It will return 
{
	"msg":"Sucessfully Deleted!""
}
But If the DB don't have requested link, It will return

{
	"msg":"Requested Link Not Found"
}
```

### Load Link

Load Link From Database

Frontend -> query.html

``` 
EndPoint : ServerIP:Port/api/db
Method : "GET"

Then You will get JSON Format of Database 
Including Title,URL

For example
{
	"Title":"TEST1234 - YouTube"
	"URL":"https://www.youtube.com/user/TEST1234"
}
```

### Change Password

When you first-run server, The Default Password "defaultpassword".

So is very unsafe to use.

Please change Password after install the Server.

This project use JWT to auth!

```
EndPoint : ServerIP:Port/api/password
Method : "PUT"

{
	"password":"password"
}


```

### Update

The project based on yt-dlp, sometime it have malfunction(For example: It can't download or parshing from YouTube.)

So sometime it need to get self yt-dlp library!

```
EndPoint : ServerIP:Port/api/update
Method : "Everything"

If update is successful, It will return ->

{
	"result":"Sucess"
}

But If Failed to update, It will return
{
	"result":"failed"
}
```



### Download

This project have automatically download fucntion.

But now, You can't change interval time to download.

Soon The Change time function will be update. Please wait Until new update

Now, The Update Interval is every "2Hours".



### Special Thanks to <3

[@Andrew Bae](https://github.com/andrewbae)







