import unittest
from urllib import response
import requests
import json
import bcrypt
import jwt


# For Testing Purpose
import app
from modules import db


class UnitTest(unittest.TestCase):

    def setUp(self):
        #host setup
        self.host = "http://127.0.0.1:7000"

        self.correct_json_link_request = {
            "link":"https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pQ"
        }

        self.incorrect_404_json_link_request = {
            "link":"https://www.youtube.com/channel/234234123123123"
        }
        self.incorrect_json_link_request = {
            "link":"https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pa"
        }
        self.raw_correct_url = "https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pQ"
        self.raw_correct_url_name = "Lee Dobob - YouTube"

        self.raw_incorrect_url = "https://www.youtube.com/channel/234234123123123"


        self.default_password = "defaultpassword"

        self.authpassword = {'password':'defaultpassword'}

        self.notdefaultpassword = {'password':'notdefaultpassword'}


        self.login_headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }
        self.logined_headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRydWUifQ.ujrl2ZZPJWit0WywQRUGfWkgcOndYgznNFQdd9pj1Lg"
            }     



    # #Check DB Function
    def test_db_default_password_Check(self):
        print("====DEFAULTPASSWORD initialize====")
        print(self.assertEqual(True,bcrypt.checkpw("defaultpassword".encode('UTF-8'),db.load_password()[0][0].encode('UTF-8'))))
    
    
    
    #Check Flask function
    def test_login(self):
        print("====Login Test====")
        response = requests.post(self.host+'/api/login', headers=self.login_headers ,data=json.dumps(self.authpassword))
        data = json.loads(response.text)['msg']
        self.assertEqual("true", jwt.decode(data, "yee yee ass hair cut", algorithms="HS256")['login'])

    # def status_get_code_only(self):
    #     response = requests.get(self.host+'/api/db', headers=self.logined_headers)
    #     self.assertEqual(200,response.status_code)

    def test_insert_link(self):
        #Correct Link Insert
        response = requests.post(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.correct_json_link_request))
        data = json.loads(response.text)['msg']
        print("====INSERT Link Test====")
        print(data)
        self.assertEqual("OK",data)
        self.assertEqual(200,response.status_code)
        #Incorrect(404) Link Test
        response = requests.post(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.incorrect_404_json_link_request))
        data = json.loads(response.text)['msg']
        self.assertEqual("Invaild Youtube Link",data)
        self.assertEqual(200,response.status_code)
        #Incorrect(NullChannelName) Link Test
        response = requests.post(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.incorrect_json_link_request))
        data = json.loads(response.text)['msg']
        self.assertEqual("Channel Or Playlist is unavailable.",data)
        self.assertEqual(200,response.status_code)




    def test_remove_link(self):
        jsonLoad = json.loads(requests.get(self.host+'/api/db', headers=self.logined_headers).text)
        number = jsonLoad[-1]['id']
        req = {"id":f"{number}"}
        print(json.dumps(req))
        response = requests.delete(self.host+'/api/db', headers=self.logined_headers,data=json.dumps([req]))
        print(number)
        print(response.text)
        msg = json.loads(response.text)['msg']
        print("====Remove Link Test====")
        print(msg)
        self.assertEqual(200,response.status_code)
        self.assertEqual("Sucessfully Deleted!",msg)
    
    def test_load_link(self):
        response = requests.get(self.host+'/api/db', headers=self.logined_headers)
        print("====Load Link Test====")
        print(response.text)
        self.assertEqual(200,response.status_code)


    def test_update_password(self):
        print("====Password Change Test====")
        response = requests.put(self.host+'/api/password', headers=self.logined_headers,data=json.dumps(self.authpassword))
        msg = json.loads(response.text)['msg']
        self.assertEqual("OK",msg)
        print(msg)

    def test_update_yt_dlp(self):
        print("====Update_yt-dlp_module-====")
        response = requests.post(self.host+'/api/update', headers=self.logined_headers,data=json.dumps(self.authpassword))
        msg = json.loads(response.text)['msg']
        self.assertEqual("Success!",msg)

    # app.py Function Test

    def test_youtube_url_validation(self):
        response = app.youtube_url_validation(self.raw_correct_url)
        self.assertEqual(True,response)
        response = app.youtube_url_validation(self.raw_incorrect_url)
        self.assertEqual(True,response)

    def test_linkavaliabllity(self):
        response = app.link_avaliablity(self.raw_correct_url)
        self.assertEqual(True,response)
        response = app.link_avaliablity(self.raw_incorrect_url)
        self.assertEqual(False,response)

    def test_get_channel_name(self):
        response = app.get_channel_name(self.raw_correct_url)
        self.assertEqual(self.raw_correct_url_name,response)
        response = app.get_channel_name(self.raw_incorrect_url)
        self.assertEqual(False,response)

    #download Function Test







if __name__=='__main__':
    unittest.main()



#ref https://taegyuhan.github.io/python/Python_test_Code/