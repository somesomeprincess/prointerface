#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from model import StartPreviewParam
from parameterized import parameterized


class StartPriview(unittest.TestCase):
    def setUp(self):
        CommomUtils.Connect()

    #正常情况

    @parameterized.expand(CommomUtils.StartPreviewTestCaseFromExcel('startPreview'))
    def testStartPreview(self,_,param):
        HR=HttpRequest.HttpRequest()
        data = HR.open('camera._startPreview',fingerprint=Constant.fingerprint,parameters=param)
        print(data)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNotNone(previewUrl,'获取_previewUrl失败！')
        #如何验证rtmp连接是否正常打开

    #表格异常情况，期望是错的，但目前是正常返回

    @parameterized.expand(CommomUtils.StartPreviewTestCaseFromExcel('startPreview_err'))
    @unittest.skip('2')
    def testStartPreview_abnormalParam(self, _, param):
        # HR = HttpRequest.HttpRequest()
        # data = HR.open('camera._startPreview', parameters=param)
        # self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        # self.assertTrue(data['state'] == 'exception')
        # self.assertTrue(data.has_key('error'), '获取error失败')
        HR=HttpRequest.HttpRequest()
        data = HR.open('camera._startPreview',fingerprint=Constant.fingerprint,parameters=param)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNot(previewUrl,'获取_previewUrl失败！')

    #多参数，只传一个参数等等
    @parameterized.expand([
        (
            'morepara',StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                                      stiwidth='1920', stibitrate='1000',
                                                      stiheight='960', stimode='pano',
                                                      orimime='h265', oriframe='30',
                                                      oriwidth='1920', oribitrate='15000',
                                                      oriheight='1440', saveori='false',aaaaa='bbbbbbb').getJsonData()
        ),
        ('only_one_para','"aaa":"bbbb"'),
        ('no_para','{}')
    ])
    def testStartPreview_abnormalParaminTable(self, _, param):
        # HR = HttpRequest.HttpRequest()
        # data = HR.open('camera._startPreview', parameters=param)
        # self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        # self.assertTrue(data['state'] == 'exception')
        # self.assertTrue(data.has_key('error'), '获取error失败')
        HR=HttpRequest.HttpRequest()
        data = HR.open('camera._startPreview',fingerprint=Constant.fingerprint,parameters=param)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNot(previewUrl,'获取_previewUrl失败！')


    #错误的Fingerprint
    def testStartPreview_otherabnormal(self):
        HR = HttpRequest.HttpRequest()
        param=StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                             stiwidth='1920', stibitrate='1000',
                                             stiheight='960', stimode='pano',
                                             orimime='h265', oriframe='30',
                                             oriwidth='1920', oribitrate='15000',
                                             oriheight='1440', saveori='false').getJsonData()
        data = HR.open('camera._startPreview',fingerprint='',parameters=param)
        print(data)
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('error'), '获取error失败')

    # 过期的Fingerprint,不确定是否能实现
    def testStartPreview_otherabnormalParam(self):
        oldFP=Constant.fingerprint
        CommomUtils.DisConnect()
        CommomUtils.Connect()
        HR = HttpRequest.HttpRequest()
        param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                               stiwidth='1920', stibitrate='1000',
                                               stiheight='960', stimode='pano',
                                               orimime='h265', oriframe='30',
                                               oriwidth='1920', oribitrate='15000',
                                               oriheight='1440', saveori='false').getJsonData()
        data = HR.open('camera._startPreview', fingerprint=oldFP, parameters=param)
        print(data)
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('error'), '获取error失败')

    def tearDown(self):
        HR = HttpRequest.HttpRequest()
        HR.open("camera._stopPreview")
















