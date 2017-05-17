#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
from model import StartPreviewParam
import unittest
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')

class GetStoragePath(unittest.TestCase):
    def testGetStoragePath_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                               stiwidth='1920', stibitrate='1000',
                                               stiheight='960', stimode='pano',
                                               orimime='h265', oriframe='30',
                                               oriwidth='1920', oribitrate='15000',
                                               oriheight='1440', saveori='false').getJsonData()
        preivewdata = HR.open('camera._startPreview', parameters=param)
        print(preivewdata)

        data=HR.open("camera._getStoragePath")
        print(data)
        self.assertIsNotNone(data['state'],'获取state失败！')
        self.assertTrue(data['state']=='done','state不等于done！')
        self.assertTrue(data.has_key('results'),'没有results关键字！')
        self.assertIsNotNone(data['results']['path'],'获取path失败！')

