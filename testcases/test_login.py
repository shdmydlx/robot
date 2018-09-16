
import os
import time
import unittest
import HtmlTestRunner
from ddt import ddt,data,unpack,file_data
from common.send_email import send_mail
from common.tool import getRootDir
from common.parse_data import parse_csv
from pom.loginpg import LoginPage

from time import gmtime,strftime
from selenium import webdriver


def getDay_Str():
    return strftime("%Y-%m-%d_%H_%M_%S", gmtime())


@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def tearDown(self):
        
        rootdir = getRootDir()
        screenshots_path = os.path.join(rootdir,'screenshots')
        
        #TODO 图片文件名格式为 存放在目录 2018-09/2018-09-02  2018_09_02-17_12_11.png
        time_str=getDay_Str()
        pngfile_name =os.path.join(screenshots_path,time_str+'.png')
        self.driver.save_screenshot(pngfile_name)
        
        self.driver.delete_all_cookies()


    # @data(['xiaoming','123123','fail','用户名或密码错误'],['','123123','fail','信息不完整。'])
    @data(*parse_csv())
    @unpack
    def test_login(self,username,password,status,check_msg):
        
        text = LoginPage().check_login(self.driver,username,password,status)
        self.assertEqual(check_msg,text)
        

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="report"))
    # 发送邮件
    send_mail()