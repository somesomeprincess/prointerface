#coding:utf-8
import threading

from time import ctime,sleep
from ProUtils import HttpRequest
from ProUtils import CommomUtils
import random


def sendHeart():
    while True:
        print('sendHeart----------%s'%ctime())
        sleep(2)

def sendTakePic():
    for i in range(2):
        print('sendTakePic---------%s'%ctime())
        sleep(8)

def sendPicAndRecord():
    for i in range(100):
        print('sendTakePic---------%s' % ctime())
        sleep(10)

        print('startrecord---------%s' % ctime())
        sleep(random.randint(10, 20))
        print('endRecord')
        sleep(10)


def TakePic(num):
    for i in range(num):
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
t2=threading.Thread(target=TakePic,args=100)
threads.append(t2)
t3=threading.Thread(target=Record)
t4=threading.Thread(target=PicAndRecord)
t5=threading.Thread(target=sendPicAndRecord)
t6=threading.Thread(target=sendHeart)
if __name__=='__main__':
    #CommomUtils.Connect()
    mode=4
    if(mode==1):
        t1.setDaemon(True)
        t2.setDaemon(True)

        t1.start()
        t2.start()
        t1.join()
        t2.join()
    elif(mode==2):
        t1.setDaemon(True)
        t3.setDaemon(True)

        t1.start()
        t3.start()
        t1.join()
        t3.join()
    elif(mode==3):
        t1.setDaemon(True)
        t4.setDaemon(True)

        t1.start()
        t4.start()
        t1.join()
        t4.join()
    elif (mode == 4):
        t6.setDaemon(True)
        t5.setDaemon(True)

        t6.start()
        t5.start()
        t6.join()
        t5.join()

    print('\nall over %s'%ctime())