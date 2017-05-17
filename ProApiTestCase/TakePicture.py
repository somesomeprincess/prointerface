#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from parameterized import parameterized
from model import TakePicture
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')


class TakePicture(unittest.TestCase):
    def setUp(self):
        CommomUtils.Connect()


    #正常情况
    @parameterized.expand(CommomUtils.TakePicTestCaseFromExcel('takePicture_ok'))
    def testTakePicture_normal(self,_,param):


        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._takePicture",parameters=param)
        #持续心跳包
        CommomUtils.HeartThread()
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'done', 'state不等于done')
        id = data['results']['id']
        self.assertIsNotNone(id, 'id等于空')

    #异常情况,相机还是返回成功
    @parameterized.expand(CommomUtils.TakePicTestCaseFromExcel('takePicture_err'))
    @unittest.skip('abnormal')
    def testTakePicture_abnormal(self,_,param):
        HR=HttpRequest.HttpRequest()

        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=param)
        print(data)
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'done', 'state不等于done')
        id = data['results']['id']
        self.assertIsNotNone(id, 'id等于空')


    def testTakePicture_noFP(self):
        HR=HttpRequest.HttpRequest()

        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=sub_data,fingerprint='')
        print(data)
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'exception', 'state不等于exception')


    #多参数，只传一个参数等等
    @parameterized.expand([
        (
            'morepara',TakePicture.TakePicture(stimime='h264', stiframe='30',
                                                      stiwidth='1920', stibitrate='1000',
                                                      stiheight='960', stimode='pano',
                                                      orimime='h265', oriframe='30',
                                                      oriwidth='1920', oribitrate='15000',
                                                      oriheight='1440', saveori='false',aaaaa='bbbbbbb').getJsonData()
        ),
        ('only_one_para','{"aaa":"bbbb"}'),
        ('no_para','{}')
    ])
    @unittest.skip('dd')
    def testTakePicture_abnormalParaminTable(self, _, param):
        HR = HttpRequest.HttpRequest()
        data = HR.open('camera._startPreview', parameters=param)
        self.assertIsNotNone(data, '获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'error')
        self.assertTrue(data.has_key('error'), '获取error失败')






