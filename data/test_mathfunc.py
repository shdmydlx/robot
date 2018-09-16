import sys
sys.path.append("F:\\微信文件\\WeChat Files\\li531808264\\Files\\datadriver_demo")
import unittest
from  testcases.mathfunc import *
from ddt import ddt,data,unpack,file_data

class TestMathFunc (unittest.TestCase):


    def test_add(self):

       self.asserEqual(3,add(1,2))
       self.asserNOTEqual(3,add(2,2))

    def test_minus(self):
        self.asserEqual(1,minus(3,2))

    def test_multi(self):
        self.asserEqual(6,multi(2,3))

    def test_divide(self):
        self.asserEqual(3,divide(6,2))
        self.asserEqual(2.5,divide(5,2))

if __name__ == '__main__':
    unittest.main(verbosity=2)




