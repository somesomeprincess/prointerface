#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')

#文档写idle状态才会done
class StartQRCodeScan(unittest.TestCase):
    def testStartQRCodeScan_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._startQRCodeScan")
        self.assertIsNotNone(data['state'],'获取state失败！')
        self.assertTrue(data['state']=='done','state不等于done！')

    def testStartQRCodeScan_fail(self):
        CommomUtils.Connect()
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._startQRCodeScan",fingerprint='')
        self.assertIsNotNone(data['state'], '获取state失败！')
        self.assertTrue(data['state'] == 'exception', 'state不等于exception！')
        self.assertTrue(data.has_key('error'), '没有error关键字！')
        self.assertIsNotNone(data['error']['description'], '获取error description失败！')
        self.assertIsNotNone(data['error']['code'], '获取error code失败！')

