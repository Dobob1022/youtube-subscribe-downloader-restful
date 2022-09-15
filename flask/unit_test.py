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
        self.login_headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }
        self.delete_link = [{"id":"1"}]
        self.logined_headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRydWUifQ.ujrl2ZZPJWit0WywQRUGfWkgcOndYgznNFQdd9pj1Lg"
            }     



    # #Check DB Function
    # def test_db_default_password_Check(self):
    #     self.assertEqual(True,bcrypt.checkpw("defaultpassword".encode('UTF-8'),db.load_password()[0][0].encode('UTF-8')))
    
    # def test_password_change(self):
    #     self.assertEqual("OK",db.change_pw(bcrypt.hashpw(self.default_password.encode('UTF-8'),bcrypt.gensalt()).decode('UTF-8'))['msg'])

    # def test_insert_link_function(self):
    #     self.assertEqual("OK", db.insert_link(self.raw_correct_url,self.raw_correct_url_name)['msg'])
    #     db.delete_link("a")
        

    # def test_duplicate_insert_link_function(self):
    #     self.assertEqual("Link is duplicated!", db.insert_link(self.raw_correct_url,self.raw_correct_url_name)['msg'])

    # # def test_password_not_change(self):
    # #     self.assertEqual("Not_Changed",db.change_pw(bcrypt.hashpw(self.default_password.encode('UTF-8'),bcrypt.gensalt()).decode('UTF-8'))['msg'])
    
    
    #Check Flask function
    def test_login(self):
        response = requests.post(self.host+'/api/login', headers=self.login_headers ,data=json.dumps(self.authpassword))
        data = json.loads(response.text)['msg']
        self.assertEqual("true", jwt.decode(data, "yee yee ass hair cut", algorithms="HS256")['login'])

    def status_get_code_only(self):
        response = requests.get(self.host+'/api/db', headers=self.logined_headers)
        self.assertEqual(200,response.status_code)

    def test_insert_link(self):
        response = requests.post(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.correct_json_link_request))
        # data = json.loads(response.text)['msg']
        print(response.text)
        # self.assertEqual("OK",data)
        self.assertEqual(200,response.status_code)
    def test_remove_link(self):
        response = requests.delete(self.host+'/api/db', headers=self.logined_headers,data=json.dumps(self.delete_link))
        print(response.text)





if __name__=='__main__':
    unittest.main()



#ref https://taegyuhan.github.io/python/Python_test_Code/