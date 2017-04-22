#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils


class getOffset(unittest.TestCase):


    def testGetoffset(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._getOffset",fingerprint=Constant.fingerprint)
        print(data)
        self.assertIsNotNone(data,'获取data失败！data:%s'%data)
        self.assertTrue(data['state']=='done')
        self.assertTrue(data.has_key('results'), '获取results失败')
        pano4_3=data['results']['offset_pano_4_3']
        self.assertIsNot(pano4_3,'获取pano4_3失败！')
        pano16_9 = data['results']['offset_pano_16_9']
        self.assertIsNot(pano16_9, '获取pano16_9失败！')
        _3dleft = data['results']['offset_3d_left']
        self.assertIsNot(_3dleft, '获取offset_3d_left失败！')
        _3dright = data['results']['offset_3d_right']
        self.assertIsNot(_3dright, '获取offset_3d_right失败！')

    #错误的Fingerprint
    def testGetoffset_otherabnormal(self):
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._getOffset",fingerprint='')
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'exception')
        self.assertTrue(data.has_key('error'), '获取error失败')

