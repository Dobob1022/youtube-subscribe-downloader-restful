# youtube-subscribe-downloader-restful

## 간단한 토이프로젝트입니다!

모든 통신은 RESTful API와 JSON으로 이루어집니다!

### 프로젝트 구성에 사용된 것들

Backend - Python(Flask),yt_dlp,ETC...

Frontend - HTML+Bootstrap+Jquery

## docker 로케이션

docker-compose.yml 파일 안에 

이부분을 볼 수 있습니다.
```
volumes:
            - "HostPath:/app/download" #download folder
            - "HostPath:/app/db" #db backup
```
HostPath에 실제 저장이 될 로케이션을 지정해 주시기 바랍니다.


### 링크 추가하기

채널과 플레이리스트를 지원합니다!

```
EndPoint : ServerIP:Port/api/db
Method : "POST"

포멧은 다음과 같습니다. ->
{
  "link":"youtube_link(Channel or Playlist)"
}

링크가 이미 데이터베이스 안에 있으면

다음을 반환합니다.
{
  "result": "duplicated"
}

만약 새로운 링크라면?
{
  "result": "OK"
}
을 반환합니다.
```

### 링크 지우기

```
EndPoint : ServerIP:Port/api/db
Method : "DELETE"

요청은 다음과 같습니다

{
	"id":"listID"
}

요청이 성공적으로 진행되면 반환은 다음과 같습니다.
{
	"msg":"Sucessfully Deleted!""
}

하지만, 요청한 링크가 없다면, 다음과 같이 반환됩니다.

{
	"msg":"Requested Link Not Found"
}
```

### 링크 불러오기

링크 모음을 데이터베이스에서 불러옵니다.

Frontend -> query.html

``` 
EndPoint : ServerIP:Port/api/db
Method : "GET"


JSON형식으로 데이터베이스에서 다음을 불러옵니다.
Title,URL

예를들어
{
	"Title":"TEST1234 - YouTube"
	"URL":"https://www.youtube.com/user/TEST1234"
}
```

### 비밀번호 바꾸기

When you first-run server, The Default Password "defaultpassword".

처음 서버를 부팅하게 되면, 기본 비밀번호는 "defaultpassword"를 사용합니다.

매우 취약하기 때문에, 서버를 처음 실행 후 비밀번호를 바꿔주시기 바랍니다.

또한, JWT를 사용합니다.

```
EndPoint : ServerIP:Port/api/password
Method : "PUT"

{
	"password":"password"
}

```

### 업데이트

이 프로젝트는 yt-dlp를 사용합니다. 하지만 라이브러리가 제대로 작동하지 않는 경우가 있기에, (예를들어, 유튜브에서 영상을 다운 받지 못하는 경우)  yt-dlp 라이브러리에 업데이트가 필요로합니다.

```
EndPoint : ServerIP:Port/api/update
Method : "POST"

업데이트가 성공적으로 완료가 되면, ->

{
	"result":"Success!"
}
가 반환이 되며, 업데이트가 실패한 경우는
{
	"result":"failed"
}
가 반환이 됩니다.
```



### 다운로드

이 프로젝트는 자동으로 다운로드 하는 기능이 있습니다.

하지만, 현재는 다운로드의 시간을 조절 할 수 없습니다.

조만간 업데이트를 통하여, 다운로드 빈도를 조절 할 수 있게 수정 할 예정입니다.

현재 다운로드 빈도는 "2시간"입니다.

### Special Thanks to <3

[@Andrew Bae](https://github.com/andrewbae)







