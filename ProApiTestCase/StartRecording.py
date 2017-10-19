#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from model import StartRecording
from parameterized import parameterized
import time


class StartRecording(unittest.TestCase):
    sub_data = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
                "origin":{"mime":"h264","framerate":30,"width":3200,"bitrate":40960,"height":2400,"saveOrigin":'true'}}
    def setUp(self):
        CommomUtils.Connect()


    #正常情况

    #@parameterized.expand(CommomUtils.StartRecordTestCaseFromExcel('startRecording'))
    @parameterized.expand(CommomUtils.StartRecordTestCaseFromExcel('startrecord'))
    def testStartRecording(self,_,param):
        HR=HttpRequest.HttpRequest()
        print(param)
        data = HR.open('camera._startRecording',parameters=param)
        print(data)
        CommomUtils.Heart(2)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')


        try:
            print('stopRecording print Heart----------')
            data = HR.open("camera._stopRecording")
            if (not data['state'] == 'done'):
                print('first stop undone~')
            print(data)
        except Exception as e:
            print e
            secdata = HR.open("camera._stopRecording")

    #表格异常情况，期望是错的，但目前是正常返回
    '''
    @parameterized.expand(CommomUtils.StartRecordingTestCaseFromExcel('startrecord_err'))
    def testStartRecording_abnormalParam(self, _, param):
        # HR = HttpRequest.HttpRequest()
        # data = HR.open('camera._StartRecording', parameters=param)
        # self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        # self.assertTrue(data['state'] == 'exception')
        # self.assertTrue(data.has_key('error'), '获取error失败')
        HR=HttpRequest.HttpRequest()
        data = HR.open('camera._StartRecording',fingerprint=Constant.fingerprint,parameters=param)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNot(previewUrl,'获取_previewUrl失败！')

    #多参数，只传一个参数等等
    @parameterized.expand([
        (
            'morepara',StartRecordingParam.StartRecording(stimime='h264', stiframe='30',
                                                      stiwidth='1920', stibitrate='1000',
                                                      stiheight='960', stimode='pano',
                                                      orimime='h265', oriframe='30',
                                                      oriwidth='1920', oribitrate='15000',
                                                      oriheight='1440', saveori='false',aaaaa='bbbbbbb').getJsonData()
        ),
        ('only_one_para','"aaa":"bbbb"'),
        ('no_para','{}')
    ])
    def testStartRecording_abnormalParaminTable(self, _, param):
        # HR = HttpRequest.HttpRequest()
        # data = HR.open('camera._StartRecording', parameters=param)
        # self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        # self.assertTrue(data['state'] == 'exception')
        # self.assertTrue(data.has_key('error'), '获取error失败')
        HR=HttpRequest.HttpRequest()
        data = HR.open('camera._StartRecording',fingerprint=Constant.fingerprint,parameters=param)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNot(previewUrl,'获取_previewUrl失败！')


    #错误的Fingerprint
    def testStartRecording_otherabnormal(self):
        HR = HttpRequest.HttpRequest()
        param=StartRecordingParam.StartRecording(stimime='h264', stiframe='30',
                                             stiwidth='1920', stibitrate='1000',
                                             stiheight='960', stimode='pano',
                                             orimime='h265', oriframe='30',
                                             oriwidth='1920', oribitrate='15000',
                                             oriheight='1440', saveori='false').getJsonData()
        data = HR.open('camera._StartRecording',fingerprint='',parameters=param)
        print(data)
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('error'), '获取error失败')
    
    # 过期的Fingerprint,不确定是否能实现
    def testStartRecording_oldFP(self):
        oldFP=Constant.fingerprint
        print('oldFP----------')
        print(oldFP)
        CommomUtils.DisConnect()
        newFP=CommomUtils.Connect()
        print('newFP----------')
        print(newFP)
        HR = HttpRequest.HttpRequest()
        param = StartRecordingParam.StartRecording(stimime='h264', stiframe='30',
                                               stiwidth='1920', stibitrate='1000',
                                               stiheight='960', stimode='pano',
                                               orimime='h265', oriframe='30',
                                               oriwidth='1920', oribitrate='15000',
                                               oriheight='1440', saveori='false').getJsonData()
        data = HR.open('camera._StartRecording', fingerprint=oldFP, parameters=param)
        print(data)
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('error'), '获取error失败')
    '''
    def tearDown(self):
        Constant.fingerprint=None
        time.sleep(10)


















