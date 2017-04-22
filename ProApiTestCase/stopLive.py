#coding:utf-8
from ProUtils import HttpRequest,CommomUtils,Constant
import unittest

#待机状态下会报错
class StopLive(unittest.TestCase):
    param = {
        "audio": {"bitrate": 128, "mime": "aac", "samplerate": 48000, "sampleFormat": "s16", "channelLayout": "stereo"},
        "origin": {"mime": "h264", "framerate": 30, "width": 2560, "bitrate": 20480, "height": 1440,
                   "saveOrigin": 'false'},
        "stiching": {"mime": "h264", "mode": "pano", "framerate": 30, "width": 3840, "bitrate": 15360, "height": 1920,
                     "_liveUrl": "rtmp://127.0.0.1/live/live"}}
    # 先请求了startRecord,请求成功
    def testStopLive_ok(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()

        start = HR.open("camera._stopLive",self.param)
        if (start['state'] == 'done'):
            data = HR.open("camera._stopRecording")
            self.assertIsNotNone(data, u'获取data失败！data:%s' % data)
            self.assertTrue(data['state'] == 'done')

    # 直接请求，请求失败
    def testStopLive_nostart(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        data = HR.open("camera._stopLive")
        print(data)
        self.assertIsNotNone(data, u'获取data失败！data:%s' % data)
        self.assertTrue(data['state'] == 'error')
        err=data['error']
        self.assertIsNotNone(err['error'], u'获取error失败')
        self.assertIsNotNone(err['description'], u'获取description失败')
        self.assertIsNotNone(err['code'], u'获取code失败')

    # 错误的Fingerprint
    def stopStopLive_errFP(self):
        CommomUtils.Connect()
        print(Constant.fingerprint)
        HR = HttpRequest.HttpRequest()
        start = HR.openCommon(self.param)
        if (start['state'] == 'done'):
            data = HR.open("camera._stopLive", fingerprint='')
            self.assertIsNotNone(data, '获取data失败！data:%s' % data)
            self.assertTrue(data['state'] == 'exception')
            err = data['error']
            self.assertIsNotNone(err['error'], '获取error失败')
            self.assertIsNotNone(err['description'], '获取description失败')
            self.assertIsNotNone(err['code'], '获取code失败')