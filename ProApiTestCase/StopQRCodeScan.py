#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest
#文档写idle状态才会done
class StopQRCodeScan(unittest.TestCase):
    #开了start后请求
    def testStartQRCodeScan_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        start = HR.open("camera._startRecording", self.param)
        if (start['state'] == 'done'):
            data=HR.open("camera._stopQRCodeScan")
            self.assertIsNotNone(data['state'],'获取state失败！')
            self.assertTrue(data['state']=='done','state不等于done！')

    #直接请求
    def testStopQRCodeScan_fail(self):
        CommomUtils.Connect()
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._stopQRCodeScan")
        self.assertIsNotNone(data['state'], '获取state失败！')
        self.assertTrue(data['state'] == 'done', 'state不等于done！')

    #错误fingerprint
    def testStopQRCodeScan_wrongFP(self):
        CommomUtils.Connect()
        HR = HttpRequest.HttpRequest()
        start = HR.open("camera._startRecording", self.param)
        if (start['state'] == 'done'):
            data = HR.open("camera._stopQRCodeScan",fingerprint='')
            self.assertIsNotNone(data['state'], '获取state失败！')
            self.assertTrue(data['state'] == 'exception', 'state不等于exception！')
            self.assertTrue(data.has_key('error'), '没有error关键字！')
            self.assertIsNotNone(data['error']['description'], '获取error description失败！')
            self.assertIsNotNone(data['error']['code'], '获取error code失败！')

