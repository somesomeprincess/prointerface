#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest

class QueryState(unittest.TestCase):
    def testQueryState_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._getVersion")
        self.assertIsNotNone(data['state'],'获取state失败！')
        self.assertTrue(data['state']=='done','state不等于done！')
        self.assertTrue(data.has_key('results'),'没有results关键字！')
        results=data['results']
        self.assertIsNotNone(results,'获取results失败！')


