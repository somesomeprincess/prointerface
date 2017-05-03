#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from model import StartPreviewParam
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')

class stopPreview(unittest.TestCase):
    def setUp(self):
        CommomUtils.Connect()
    @unittest.skip('aa')
    #先请求了startPreview,请求成功
    def teststopPreview_ok(self):
        HR=HttpRequest.HttpRequest()
        param=StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                             stiwidth='1920', stibitrate='1000',
                                             stiheight='960', stimode='pano',
                                             orimime='h265', oriframe='30',
                                             oriwidth='1920', oribitrate='15000',
                                             oriheight='1440', saveori='false').getJsonData()
        start = HR.open('camera._startPreview',param)
        if(start['state']=='done'):
            data=HR.open("camera._stopPreview")
            self.assertIsNotNone(data,u'获取data失败！data:%s'%data)
            self.assertTrue(data['state']=='done')


    # 直接请求，请求失败
    @unittest.skip('aas')
    def teststopPreview_notok(self):
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._stopPreview")
        print(data)
        self.assertIsNotNone(data, u'获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'error')
        self.assertTrue(data.has_key('error'), '没有error关键字')
        self.assertIsNotNone(data['name'], '获取name失败')
        error = data['error']
        self.assertIsNotNone(error['description'], '获取description失败')
        self.assertIsNotNone(error['code'], '获取code失败')



    #错误的Fingerprint
    def teststopPreview_errFP(self):
        HR=HttpRequest.HttpRequest()
        param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                               stiwidth='1920', stibitrate='1000',
                                               stiheight='960', stimode='pano',
                                               orimime='h265', oriframe='30',
                                               oriwidth='1920', oribitrate='15000',
                                               oriheight='1440', saveori='false').getJsonData()
        start = HR.open("camera._startPreview",parameters=param)
        if (start['state']=='done'):
            data=HR.open("camera._stopPreview",fingerprint='')
            self.assertIsNotNone(data,'获取data失败！data:%s'%data)
            self.assertTrue(data['state']=='exception')
            '''
            self.assertTrue(data.has_key('error'),'没有error关键字')
            error=data['error']
            self.assertIsNotNone(error['name'], '获取errorname失败')
            self.assertIsNotNone(error['description'], '获取description失败')
            self.assertIsNotNone(error['code'], '获取code失败')
            '''

