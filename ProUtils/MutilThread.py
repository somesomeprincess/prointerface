#coding:utf-8
import threading
from multiprocessing import Process
from time import ctime,sleep
from ProUtils import HttpRequest
from ProUtils import CommomUtils
import random
import unittest
from parameterized import parameterized





def sendPicAndRecord():
    for i in range(100):
        print('sendTakePic---------%s' % ctime())
        sleep(10)

        print('startrecord---------%s' % ctime())
        sleep(random.randint(10, 20))
        print('endRecord')
        sleep(10)


def TakePic():
    for i in range(10):
        print('TakePic')
        # 发送TakePicture请求
        HR = HttpRequest.HttpRequest()
        # HR.getFingerPrint()
        sub_data = {"origin": {"mime": "jpeg", "framerate": None, "width": 4000, "bitrate": None, "height": 3000,
                               "saveOrigin": 'true'},
                    "stiching": {"mime": "jpeg", "framerate": None, "width": 7680, "bitrate": None, "height": 3840,
                                 "mode": "pano"}}
        data = HR.open("camera._takePicture", parameters=sub_data)
        print(data)
        sleep(10)

def Record():
    for i in range():
        print('StartRecording')
        # 发送TakePicture请求
        HR = HttpRequest.HttpRequest()
        # HR.getFingerPrint()
        sub_data = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
                    "origin":{"mime":"h264","framerate":30,"width":3200,"bitrate":40960,"height":2400,"saveOrigin":'true'}}
        data = HR.open("camera._startRecording", parameters=sub_data)
        print(data)
        sleep(random.randint(10,20))
        enddata=HR.open("camera._endRecording")
        print(enddata)

def PicAndRecord():
    for i in range(100):
        HR = HttpRequest.HttpRequest()
        # HR.getFingerPrint()
        sub_data = {"origin": {"mime": "jpeg", "framerate": None, "width": 4000, "bitrate": None, "height": 3000,
                               "saveOrigin": 'true'},
                    "stiching": {"mime": "jpeg", "framerate": None, "width": 7680, "bitrate": None, "height": 3840,
                                 "mode": "pano"}}
        data = HR.open("camera._takePicture", parameters=sub_data)
        print(data)
        sleep(10)

        sub_data_rec = {
            "audio": {"bitrate": 128, "mime": "aac", "samplerate": 48000, "sampleFormat": "s16", "channelLayout": "stereo"},
            "origin": {"mime": "h264", "framerate": 30, "width": 3200, "bitrate": 40960, "height": 2400,
                       "saveOrigin": 'true'}}
        recdata = HR.open("camera._startRecording", parameters=sub_data_rec)
        print(recdata)
        sleep(random.randint(10, 20))
        enddata = HR.open("camera._endRecording")
        print(enddata)
        sleep(10)

def Heart():
    while True:
        print('Heart')
        CommomUtils.Connect()
        sleep(3)


threads=[]
t1=threading.Thread(target=Heart)
threads.append(t1)
t2=threading.Thread(target=TakePic)
threads.append(t2)
t3=threading.Thread(target=Record)
t4=threading.Thread(target=PicAndRecord)
t5=threading.Thread(target=sendPicAndRecord)


def sendHeart():
    for i in range(5):
        print('sendHeart----------%s' % ctime())
        sleep(2)


def sendPic():
    for i in range(10):
        print('sendTakePic---------%s' % ctime())
        sleep(10)


class MutilThread(unittest.TestCase):


    # 正常情况
    @parameterized.expand(CommomUtils.TakePicTestCaseFromExcel('takePicture_ok'))
    def testTakePicture_normal(self, _, param):
        print(param)
        t6 = threading.Thread(target=sendHeart)
        #t6 = Process(target=sendHeart)
        t6.start()
        t6.join()



        # HR = HttpRequest.HttpRequest()
        # data = HR.open("camera._takePicture", parameters=param)
        # print(data)
        # self.assertIsNotNone(data, u'data为空！%s' % data)
        # self.assertTrue(data['state'] == 'done', 'state不等于done')
        # id = data['results']['id']
        # self.assertIsNotNone(id, 'id等于空')


    # def testOne(self):
    #     t5 = threading.Thread(target=sendTakePic)
    #     t5.setDaemon(True)
    #     t5.start()
    #     t5.join()
if __name__=='__main__':
    ps=MutilThread('startPreview')
    print(ps)