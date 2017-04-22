#coding:utf-8
from ProUtils import HttpRequest,CommomUtils,Constant
import unittest

#待机状态下会报错
class GetImageParam(unittest.TestCase):
    def testGetImageParam(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._getImageParam",fingerprint=Constant.fingerprint)
        print(data)
        self.assertTrue(data['state'] == 'done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        self.assertIsNotNone(data['results']['hue'],'获取hue失败，hue:%s'%data['results']['hue'])
        self.assertIsInstance(data['results']['hue'],int)
        self.assertIsNotNone(data['results']['aaa_mode'], '获取aaa_mode失败，aaa_mode:%s' % data['results']['aaa_mode'])
        self.assertIsInstance(data['results']['aaa_mode'],int)
        self.assertIsNotNone(data['results']['wb'], '获取wb失败，wb:%s' % data['results']['wb'])
        self.assertIsInstance(data['results']['wb'],int)
        self.assertIsNotNone(data['results']['iso_value'], '获取hue失败，iso_value:%s' % data['results']['iso_value'])
        self.assertIsInstance(data['results']['iso_value'], int)
        self.assertIsNotNone(data['results']['shutter_value'], '获取shutter_value失败，shutter_value:%s' % data['results']['shutter_value'])
        self.assertIsInstance(data['results']['shutter_value'], int)
        self.assertIsNotNone(data['results']['brightness'], '获取brightness失败，brightness:%s' % data['results']['brightness'])
        self.assertIsInstance(data['results']['brightness'], int)
        self.assertIsNotNone(data['results']['contrast'], '获取contrast失败，contrast:%s' % data['results']['contrast'])
        self.assertIsInstance(data['results']['contrast'], int)
        self.assertIsNotNone(data['results']['saturation'], '获取saturation失败，saturation:%s' % data['results']['saturation'])
        self.assertIsInstance(data['results']['saturation'], int)
        self.assertIsNotNone(data['results']['sharpness'], '获取sharpness失败，sharpness:%s' % data['results']['sharpness'])
        self.assertIsInstance(data['results']['sharpness'], int)
        self.assertIsNotNone(data['results']['ev_bias'], '获取ev_bias失败，ev_bias:%s' % data['results']['ev_bias'])
        self.assertIsInstance(data['results']['ev_bias'], int)
        self.assertIsNotNone(data['results']['ae_meter'], '获取ae_meter失败，hue:%s' % data['results']['ae_meter'])
        self.assertIsInstance(data['results']['ae_meter'], int)


    #错误的Fingerprint

    def testGetImageParam_otherabnormal(self):
        CommomUtils.Connect()
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._getOffset",fingerprint='')
        print(data)
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('error'), '获取error失败')
        err_descri=data['error']['description']
        self.assertIsNotNone(err_descri,u'获取错误描述失败！description:%s'%err_descri)
        err_code=data['error']['code']
        self.assertIsNotNone(err_code,'获取错误码失败！code:%s'%err_code)
        self.assertTrue(err_code=='invalidParameterValue')