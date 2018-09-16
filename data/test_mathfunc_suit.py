import unittest
from data.test_mathfunc import TestMathFunc
from ddt import ddt,data,unpack,file_data
import HtmlTestRunner
from unittest import TestLoader,TestSuite


if __name__ == '__main__':

#生成文件结果  
#用addTests + TestLoader
    suite = unittest.TestSuite()
#LoadTestFromName(),传入‘模块名.TestCase’
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    with open('unittestTextReport.txt','a')as f:

        runner = unittest.TextTestRunner(strem=f,verbosity=2)
        runner.run(suite)
