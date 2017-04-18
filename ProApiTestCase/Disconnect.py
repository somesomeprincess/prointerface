#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant
import unittest

class Disconnect(unittest.TestCase):
    def atestDisconneact(self):
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._disconnect")
        print(Constant.fingerprint)
        self.assertIsNotNone(data,'获取data失败')
        print(data)