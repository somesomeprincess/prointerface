#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest

class Disconnect(unittest.TestCase):
    def testDisconneact(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._disconnect")
        print(Constant.fingerprint)
        self.assertIsNotNone(data,'获取data失败')
        print(data)