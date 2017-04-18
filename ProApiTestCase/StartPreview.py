#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,HeartBeat
from model import StartPreviewParam
from parameterized import parameterized

class StartPriview(unittest.TestCase):
    @parameterized.expand([
        ('normal_h264', StartPreviewParam.StartPreviewParam(stimode='h264').getJsonData()),
        ('normal_h265', StartPreviewParam.StartPreviewParam(stimode='h265', oriheight='ds').getJsonData())

    ])
    def testStartPreview(self,_,param):
        self.Connect()
        print(Constant.fingerprint)
        HR=HttpRequest.HttpRequest()

        data=HR.open("camera._startPreview",parameters=param)
        print('data = %s'%data)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNot(previewUrl,'获取_previewUrl失败！')



    def Connect(self):
        isconnect = HeartBeat.HeartBeat().IsConnect()
        if (not isconnect):
            HeartBeat.HeartBeat().IsConnect()


    def ConnectWhile(self):
        while True:
            if (HeartBeat.HeartBeat().IsConnect()):
                break




