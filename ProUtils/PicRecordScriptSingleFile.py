#coding:utf-8
import random
import threading
from time import ctime, sleep


from ProUtils import HttpRequest


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
        sleep(7)

def TakePic(num):
    for i in range(num):
        takePicAction()

def takePicAction():
    print('TakePic')
    sleep(2)
    # 发送TakePicture请求
    HR = HttpRequest.HttpRequest()
    # HR.getFingerPrint()
    datalist = []
    sub_data = {"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},
                "stiching": {"mime": "jpeg",  "width": 7680,  "height": 3840,"mode": "pano"}}

    data8k3d = {"origin": {"saveOrigin": 'true', "height": 3000, "mime": "jpeg", "width": 4000}, "delay": 5, "stiching": {"mode": "3d_top_left", "height": 7680, "mime": "jpeg", "width": 7680}}
    data_burst={"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},
                "stiching": {"mime": "jpeg",  "width": 7680,  "height": 3840,"mode": "pano"},'delay':0,'burst':{"enable":'true',"count":3}}
    data_8kOF={"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},"stabilization":'false',"delay":0,
                "stiching": {"algorithm":"opticalFlow","bitrate":"null","framerate":"null","mime":"jpeg","height":3840,"mode":"pano","width":7680}}

    data_8k_3d_OF = {"origin": {"mime": "jpeg", "width": 4000, "height": 3000, "saveOrigin": 'true'},
                 "stabilization": 'false', "delay": 0,
                 "stiching": {"algorithm": "opticalFlow", "bitrate": "null", "framerate": "null", "mime": "jpeg",
                              "height": 7680, "mode": "3d_top_left", "width": 7680}}

    data_raw={"origin":{"framerate":'null',"bitrate":'null',"mime":"raw","height":3000,"saveOrigin":'true',"width":4000},"stabilization":'false',"delay":0}
    data_hdr={"origin":{"framerate":'null',"bitrate":'null',"mime":"jpeg","height":3000,"saveOrigin":'true',"width":4000},
              "stabilization":'false',"delay":0,"hdr":{"min_ev":-32,"count":3,"enable":'true',"max_ev":32}}
    cube={"origin":{"mime":"jpeg","width":4000,"height":3000, "saveOrigin":"true"},
                                                      "stiching":{"map":"cube","mode":"pano","mime":"jpeg","width":2880,"height":1920, "algorithm":"opticalFlow"}}


    datalist.append(sub_data)
    datalist.append(data8k3d)
    datalist.append(data_raw)
    datalist.append(data_hdr)
    datalist.append(data_burst)

    datalist.append(data_8kOF)
    datalist.append(data_8k_3d_OF)
    datalist.append(cube)



    origin_no_sti={"origin": {"bitrate": None, "width": 4000, "height": 3000, "mime": "jpeg", "saveOrigin": 'true', "framerate": None}}
    #data = HR.open("camera._takePicture", parameters=random.choice(datalist))
    data = HR.open("camera._takePicture", parameters=data_burst)
    print(data)
    CommomUtils.writeLogToFile(str(data))
    if(not data['state']=='done'):
        errstr='nowtime is'+ctime()+'\ndata is:'+str(data)
        SendEmail.send(errstr)
    sleep(30)



def Record(rangenum=5,mintime=10,maxtime=15):
    for i in range(rangenum):
        startRecord()
        randomtime=random.randint(mintime,maxtime)
        print('this time random time is %s'%randomtime)
        CommomUtils.writeLogToFile('this time random time is %s'%randomtime)
        sleep(randomtime)
        stopRecord()
        sleep(30)

def startRecord():
    print('StartRecording')

    HR = HttpRequest.HttpRequest()
    # HR.getFingerPrint()
    datalist = []
    sub_data6k = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
                "origin":{"mime":"h264","framerate":30,"width":3200,"bitrate":40960,"height":2400,"saveOrigin":'true'}}
    sub_data8k = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
                "origin":{"mime":"h264","framerate":30,"width":3840,"bitrate":40960,"height":2160,"saveOrigin":'true'}}
    sub_data4k = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
                "origin":{"mime":"h264","framerate":30,"width":2560,"bitrate":40960,"height":1440,"saveOrigin":'true'}}
    # sub_data4kstich = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
    #             "origin":{"mime":"h264","framerate":30,"width":2560,"bitrate":40960,"height":1440,"saveOrigin":'true'},
    #                    "stiching": {"width": 3840, "mime": "h264", "height": 1920, "mode": "pano", "framerate": 30,"bitrate": 40960}}
    #
    # sub_data4k3d = {"audio":{"bitrate":128,"mime":"aac","samplerate":48000,"sampleFormat":"s16","channelLayout":"stereo"},
    #             "origin":{"mime":"h264","framerate":24,"width":2560,"bitrate":25600,"height":1440,"saveOrigin":'true'},
    #                    "stiching": {"width": 3840, "mime": "h264", "height": 3840, "mode": "3d_top_left", "framerate": 24,"bitrate": 40960}}

    sub_data_timelapse={"storageSpeedTest":'false',"origin":{"framerate":30,"bitrate":20480,"width":4000,"logMode":0,"height":3000,"saveOrigin":'true',"mime":"jpeg"},
                        "stabilization":'false',"audio":{"channelLayout":"stereo","bitrate":128,"samplerate":48000,"sampleFormat":"s16","mime":"aac"},
                        "timelapse":{"enable":'true',"interval":2000},"fileOverride":'false'}

    sub_timelapse = {
        "audio": {"bitrate": 128, "mime": "aac", "samplerate": 48000, "sampleFormat": "s16", "channelLayout": "stereo"},
        "origin": {"mime": "h264", "framerate": 30, "width": 2560, "bitrate": 40960, "height": 1440,
                   "saveOrigin": 'true'}}


    datalist.append(sub_data8k)
    datalist.append(sub_data4k)
    #datalist.append(sub_data4k3d)
    datalist.append(sub_data6k)
    #datalist.append(sub_data4kstich)


    data = HR.open("camera._startRecording", parameters=random.choice(datalist))
    CommomUtils.writeLogToFile(str(data))
    if(not data['state']=='done'):
        #print(type(ctime()),type(data))
        nowtime=ctime()
        datastr=str(data)
        errstr='nowtime is'+ctime()+'\ndata is:'+datastr
        '''SendEmail.send(errstr)'''
    print(data)

def stopRecord():
    print('stoprecording---')
    HR = HttpRequest.HttpRequest()
    try:
        data = HR.open("camera._stopRecording")

        if (not data['state'] == 'done'):
        #     # print(type(ctime()),type(data))
        #     nowtime = ctime()
        #     datastr = str(data)
        #     errstr = 'nowtime is' + ctime() + '\ndata is:' + datastr
        #     print(type(nowtime), type(datastr))
        #     SendEmail.send(errstr)
            print('first stop done~')
        print(data)
        CommomUtils.writeLogToFile(str(data))
    except Exception as e:
        print e
        secdata = HR.open("camera._stopRecording")
        # if (not data['state'] == 'done'):
        #     # print(type(ctime()),type(data))
        #     nowtime = ctime()
        #     datastr = str(data)
        #     errstr = 'nowtime is' + ctime() + '\ndata is:' + datastr
        #     print(type(nowtime), type(datastr))
        #     SendEmail.send(errstr)
        print(secdata)
        CommomUtils.writeLogToFile(str(secdata))


def PicAndRecord(rangenum=3,minrecord=10,maxrecord=15):
    for i in range(rangenum):
        takePicAction()
        startRecord()
        sleep(random.randint(minrecord, maxrecord))
        stopRecord()
        sleep(25)

def Heart(sleeptime=3):
    while True:
        CommomUtils.writeLogToFile('Heart')
        print('Heart')
        CommomUtils.Connect()
        sleep(sleeptime)

tHeart=threading.Thread(target=Heart)
t2Pic=threading.Thread(target=TakePic,args=(4030,))
t3Record=threading.Thread(target=Record,args=(1025,10,12))
# tPicAndRecord=threading.Thread(target=PicAndRecord(3,10,15))
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
    mode=1
    if(mode==1):
        try:
            runThreadAs(tHeart,t2Pic)
        except Exception as e:
            '''CommomUtils.writeLogToFile(e)'''
            pass
    elif(mode==2):
        try:
            runThreadAs(tHeart, t3Record)
        except Exception as e:
            '''CommomUtils.writeLogToFile(e)'''
            pass
    # elif (mode == 4):
    #      runThreadAs(t6, t5)
    # elif(mode==5):
    #     runThreadAs(t6, tRecord)
    # elif(mode==6):
    #     runThreadAs(tHeart, tPicAndRecord)

    print('\nall over %s'%ctime())
    HR = HttpRequest.HttpRequest()
    data = HR.open("camera._disconnect")
    print(data)