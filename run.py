#coding:utf-8
import unittest
from ProUtils import ProHTMLTestRunner

if __name__=='__main__':
    suite = unittest.TestLoader().discover(start_dir='ProApiTestCase', pattern='*.py')
    with open('result.html','wb') as fp:
        runner = ProHTMLTestRunner.HTMLTestRunner(stream=fp, title='test result')
        runner.run(suite)