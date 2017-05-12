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

def sendRecord():
    print('start record----')
    sleep(15)
    print('end record---')
    sleep(5)

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
        takePicAction()

def takePicAction():
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

def Record(rangenum=5,mintime=10,maxtime=15):
    for i in range(rangenum):
        startRecord()
        sleep(random.randint(mintime,maxtime))
        stopRecord()
        sleep(5)

def startRecord():
    print('StartRecording')

    HR = HttpRequest.HttpRequest()
    # HR.getFingerPrint()
    sub_data = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
                "origin":{"mime":"h264","framerate":30,"width":3200,"bitrate":40960,"height":2400,"saveOrigin":'true'}}
    data = HR.open("camera._startRecording", parameters=sub_data)
    print(data)

def stopRecord():
    print('stoprecording---')
    HR = HttpRequest.HttpRequest()
    try:
        data = HR.open("camera._stopRecording")
        print('first stop done~')
        print(data)
    except Exception as e:
        print e
        secdata = HR.open("camera._stopRecording")
        print(secdata)


def PicAndRecord(rangenum=3,minrecord=10,maxrecord=15):
    for i in range(rangenum):
        takePicAction()
        startRecord()
        sleep(random.randint(minrecord, maxrecord))
        stopRecord()
        sleep(5)

def Heart(sleeptime=3):
    while True:
        print('Heart')
        CommomUtils.Connect()
        sleep(sleeptime)

tHeart=threading.Thread(target=Heart)
t2Pic=threading.Thread(target=TakePic,args=(3,))
t3Record=threading.Thread(target=Record,args=(5,10,15))
tPicAndRecord=threading.Thread(target=PicAndRecord(3,10,15))
t5=threading.Thread(target=sendPicAndRecord)
t6=threading.Thread(target=sendHeart)
tRecord=threading.Thread(target=sendRecord)


def runThreadAs(thread1,thread2):
    #thread1 sends heart-package
    thread1.setDaemon(True)
    thread1.start()
    thread2.start()
    thread2.join()


if __name__=='__main__':
    CommomUtils.Connect()
    mode=6
    if(mode==1):
        runThreadAs(tHeart,t2Pic)
    elif(mode==2):
        runThreadAs(tHeart, t3Record)
    elif(mode==3):
        tHeart.setDaemon(True)
        tHeart.start()
        t2Pic.start()
        tRecord.start()
        t2Pic.join()
        tRecord.join()
    elif (mode == 4):
        runThreadAs(t6, t5)
    elif(mode==5):
        runThreadAs(t6, tRecord)
    elif(mode==6):
        runThreadAs(tHeart, tPicAndRecord)

    print('\nall over %s'%ctime())
    HR = HttpRequest.HttpRequest()
    data = HR.open("camera._disconnect")
    print(data)