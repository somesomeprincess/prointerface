#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,HeartBeat,CommomUtils
from model import StartPreview
from parameterized import parameterized

class StartPriview(unittest.TestCase):
    @parameterized.expand([
        ('normal_h264', StartPreview.StartPreview(stimode='h264',abd=111).getJsonData()),
        ('normal_h265', StartPreview.StartPreview(stimode='h265', oriheight='ds').getJsonData())


    ])
    def testStartPreview(self,_,param):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._startPreview",parameters=param)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        previewUrl=data['results']['_previewUrl']
        self.assertIsNot(previewUrl,'获取_previewUrl失败！')












