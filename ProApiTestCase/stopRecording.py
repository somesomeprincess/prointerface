#coding:utf-8
from ProUtils import HttpRequest,CommomUtils,Constant
import unittest
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')
#待机状态下会报错
class StopRecording(unittest.TestCase):
    param = {"audio": {"bitrate": 128, "mime": "aac", "samplerate": 48000, "sampleFormat": "s16",
                       "channelLayout": "stereo"},
             "origin": {"mime": "h264", "framerate": 30, "width": 3200, "bitrate": 40960, "height": 2400,
                        "saveOrigin": 'true'}}

    def setUp(self):
        CommomUtils.Connect()

    # 先请求了startRecord,请求成功
    def testStopRecording_ok(self):
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        start = HR.open("camera._startRecording",self.param)
        print(start)
        data = HR.open("camera._stopRecording")
        print(data)
        self.assertIsNotNone(data, u'获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'done')

    # 直接请求，请求失败
    def testStopRecording_nostart(self):
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._stopRecording")
        print(data)
        self.assertIsNotNone(data, u'获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'error')
        err=data['error']
        self.assertIsNotNone(err['description'], u'获取description失败')
        self.assertIsNotNone(err['code'], u'获取code失败')

    # 错误的Fingerprint
    def teststopStopRecording_errFP(self):
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        start = HR.open("camera._startRecording",self.param)
        if (start['state'] == 'done'):
            data = HR.open("camera._stopRecording", fingerprint='')
            self.assertIsNotNone(data, '获取data失败！data:%s' % data)
            self.assertTrue(data['state'] == 'exception')
            err = data['error']
            self.assertIsNotNone(err['description'], '获取description失败')
            self.assertIsNotNone(err['code'], '获取code失败')