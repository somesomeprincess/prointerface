#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest

class Disconnect(unittest.TestCase):
    def testDisconneact_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._disconnect")
        self.assertIsNotNone(data['state'],'state等于空！')
        self.assertTrue(data['state']=='done','state不等于done!')

    def testDisconneact_fail(self):
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._disconnect")
        self.assertIsNotNone(data['state'], '获取state失败！')
        self.assertTrue(data['state'] == 'exception', 'state不等于exception！')
        self.assertTrue(data.has_key('error'), '没有error关键字！')
        self.assertIsNotNone(data['error']['description'], '获取error description失败！')
        self.assertIsNotNone(data['error']['code'], '获取error code失败！')