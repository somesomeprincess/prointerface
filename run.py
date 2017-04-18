#coding:utf-8
import unittest
import HTMLTestRunner
from ProUtils import BSTestRunner

if __name__=='__main__':
    suite=unittest.TestLoader().discover(start_dir='ProApiTestCase',pattern='*.py')
    with open('result.html','wb') as fp:
        #runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result')
        runner=BSTestRunner.BSTestRunner(
            stream=fp,
            title='Pro'
        )
        runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
        runner.run(suite)