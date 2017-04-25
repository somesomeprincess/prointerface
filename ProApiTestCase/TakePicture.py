#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from parameterized import parameterized
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')

class TakePicture(unittest.TestCase):
    #正常情况
    @parameterized.expand(CommomUtils.StartPreviewTestCaseFromExcel('takePicture_ok'))
    def testTakePicture_normal(self,_,param):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()

        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=param)
        print(data)
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'done', 'state不等于done')
        id = data['results']['id']
        self.assertIsNotNone(id, 'id等于空')

    #异常情况
    @parameterized.expand(CommomUtils.StartPreviewTestCaseFromExcel('takePicture_err'))
    def testTakePicture_normal(self,_,param):
        CommomUtils.Connect()
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
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()

        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=sub_data,fingerprint='')
        print(data)
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'done', 'state不等于done')
        id = data['results']['id']
        self.assertIsNotNone(id, 'id等于空')
