#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
from model import StartPreviewParam
import unittest
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')

#文档写idle状态才会done
class StartQRCodeScan(unittest.TestCase):
    def setUp(self):
        CommomUtils.Connect()

    def testStartQRCodeScan_ok(self):
        HR=HttpRequest.HttpRequest()
        param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                               stiwidth='1920', stibitrate='1000',
                                               stiheight='960', stimode='pano',
                                               orimime='h265', oriframe='30',
                                               oriwidth='1920', oribitrate='15000',
                                               oriheight='1440', saveori='false').getJsonData()
        preivewdata = HR.open('camera._startPreview', parameters=param)
        print(preivewdata)


        data=HR.open("camera._startQRCodeScan")
        print(data)
        self.assertIsNotNone(data['state'],'获取state失败！')
        self.assertTrue(data['state']=='done','state不等于done！')
    @unittest.skip('3')
    def testStartQRCodeScan_fail(self):
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._startQRCodeScan",fingerprint='')
        self.assertIsNotNone(data['state'], '获取state失败！')
        self.assertTrue(data['state'] == 'exception', 'state不等于exception！')
        self.assertTrue(data.has_key('error'), '没有error关键字！')
        self.assertIsNotNone(data['error']['description'], '获取error description失败！')
        self.assertIsNotNone(data['error']['code'], '获取error code失败！')

