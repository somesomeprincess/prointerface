#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from model import StartPreviewParam

class stopPreview(unittest.TestCase):

    #先请求了startPreview,请求成功
    def teststopPreview_ok(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR=HttpRequest.HttpRequest()
        param=StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                             stiwidth='1920', stibitrate='1000',
                                             stiheight='960', stimode='pano',
                                             orimime='h265', oriframe='30',
                                             oriwidth='1920', oribitrate='15000',
                                             oriheight='1440', saveori='false').getJsonData()
        start = HR.openCommon(param)
        if(start['state']=='done'):
            data=HR.open("camera._stopPreview")
            self.assertIsNotNone(data,u'获取data失败！data:%s'%data)
            self.assertTrue(data['state']=='done')


    # 直接请求，请求失败

    def teststopPreview_notok(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._stopPreview")
        print(data)
        self.assertIsNotNone(data, u'获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('name'), u'获取name失败')
        name = data['name']

        self.assertIsNotNone(name['error'], u'获取error失败')
        self.assertIsNotNone(name['description'], u'获取description失败')
        self.assertIsNotNone(name['code'], u'获取code失败')



    #错误的Fingerprint
    def stopPreview_errFP(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR=HttpRequest.HttpRequest()
        param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                               stiwidth='1920', stibitrate='1000',
                                               stiheight='960', stimode='pano',
                                               orimime='h265', oriframe='30',
                                               oriwidth='1920', oribitrate='15000',
                                               oriheight='1440', saveori='false').getJsonData()
        start = HR.open("camera._startPreview",param)
        if (start['state']=='done'):
            data=HR.open("camera._stopPreview",fingerprint='')
            self.assertIsNotNone(data,'获取data失败！data:%s'%data)
            self.assertTrue(data['state']=='exception')
            self.assertTrue(data.has_key('name'),'获取name失败')
            name=data['name']
            self.assertIsNotNone(name['error'], '获取error失败')
            self.assertIsNotNone(name['description'], '获取description失败')
            self.assertIsNotNone(name['code'], '获取code失败')
