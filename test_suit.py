
import unittest
import HtmlTestRunner
from common.send_email import send_mail


from unittest import TestLoader,TestSuite
loader = TestLoader()

tests = loader.discover(start_dir='./testcases',pattern='test*.py')
testsuit = TestSuite()
testsuit.addTests(tests)

runner = HtmlTestRunner.HTMLTestRunner(output="report")
runner.run(testsuit)

send_mail()