import unittest
import requests
import json
import bcrypt
import jwt


# For Testing Purpose
import app
from modules import db


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.host = "http://localhost:7000"
        self.correct_json_link_request = {
            "link":"https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pQ"
        }

        self.incorrect_json_link_request = {
            "link":"https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pa"
        }
        self.raw_correct_url = "https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pQ"
        self.raw_correct_url_name = "Lee Dobob"
        self.raw_incorrect_url = "https://www.youtube.com/channel/UCbBI8DBJe3i0zfVkNY9z5pa"


        self.default_password = "defaultpassword"

        self.authpassword = {'password':'defaultpassword'}

        self.notdefaultpassword = {'password':'notdefaultpassword'}


        self.login_headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }
        self.delete_link = [{"id":"1"}]
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

    def status_get_code_only(self):
        response = requests.get(self.host+'/api/db', headers=self.logined_headers)
        self.assertEqual(200,response.status_code)

    def test_insert_link(self):
        response = requests.post(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.correct_json_link_request))
        data = json.loads(response.text)['msg']
        print("====INSERT Link Test====")
        print(data)
        self.assertEqual("OK",data)
        self.assertEqual(200,response.status_code)

    def test_remove_link(self):
        response = requests.delete(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.delete_link))
        print(response.status_code)
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






if __name__=='__main__':
    unittest.main()



#ref https://taegyuhan.github.io/python/Python_test_Code/