#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest

class GetStoragePath(unittest.TestCase):
    def testGetStoragePath_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._getStoragePath")
        self.assertIsNotNone(data['state'],'获取state失败！')
        self.assertTrue(data['state']=='done','state不等于done！')
        self.assertTrue(data.has_key('results'),'没有results关键字！')
        self.assertIsNotNone(data['results']['path'],'获取path失败！')

