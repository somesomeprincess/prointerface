#coding:utf-8
import threading

from time import ctime,sleep
from ProUtils import HttpRequest
from ProUtils import CommomUtils,Constant
import random
import json
import urllib2


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
    startRecord()
    #sleep(random.randint(5,10))
    sleep(10)
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

    header = {'Fingerprint':  Constant.fingerprint, 'Content-Type': 'application/json', 'User-Agent': 'Apache-HttpClient/4.4',
              'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5, application/x-mpegURL'}
    jsondata = {'name': "camera._stopRecording"}
    jsondata = json.dumps(jsondata)

    request = urllib2.Request(Constant.Common_url, jsondata, headers=header)
    try:
        resp = urllib2.urlopen(request, timeout=10)
        result = resp.read()
        data = json.loads(result)
        print(data)
    except Exception as e:
        print e
        urllib2.Request(Constant.Common_url, jsondata, headers=header)




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
        sleep(random.randint(5, 10))
        enddata = HR.open("camera._stopRecording")
        print(enddata)
        sleep(10)

def Heart():
    while True:
        print('Heart')
        CommomUtils.Connect()
        sleep(3)


threads=[]
tHeart=threading.Thread(target=Heart)
threads.append(tHeart)
t2Pic=threading.Thread(target=TakePic)
threads.append(t2Pic)
t3Record=threading.Thread(target=Record)
t4=threading.Thread(target=PicAndRecord)
t5=threading.Thread(target=sendPicAndRecord)
t6=threading.Thread(target=sendHeart)
tRecord=threading.Thread(target=sendRecord)
if __name__=='__main__':
    CommomUtils.Connect()
    mode=2
    if(mode==1):
        tHeart.setDaemon(True)
        t2Pic.setDaemon(True)

        tHeart.start()
        t2Pic.start()
        tHeart.join()
        t2Pic.join()
    elif(mode==2):
        tHeart.setDaemon(True)
        t3Record.setDaemon(True)

        tHeart.start()
        t3Record.start()
        tHeart.join()
        t3Record.join()
    elif(mode==3):
        tHeart.setDaemon(True)
        t4.setDaemon(True)

        tHeart.start()
        t4.start()
        tHeart.join()
        t4.join()
    elif (mode == 4):
        t6.setDaemon(True)
        t5.setDaemon(True)

        t6.start()
        t5.start()
        t6.join()
        t5.join()
    elif(mode==5):
        t6.setDaemon(True)
        tRecord.setDaemon(True)

        t6.start()
        tRecord.start()
        t6.join()
        tRecord.join()




    print('\nall over %s'%ctime())
    HR = HttpRequest.HttpRequest()
    data = HR.open("camera._disconnect")
    print(data)