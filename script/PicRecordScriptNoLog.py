#coding:utf-8
import random,logging
import threading
from time import ctime, sleep
from ProUtils import CommomUtils, SendEmail,Constant,HttpRequest
from model import StartPreviewParam,StartLive
import xlrd,xlwt
from xlutils.copy import copy
from script.PicRecordScriptPrintTest import sendTakePic

def doPropertyRandom():
    pass



def doSetExposureRandom(property=None, option=None):
    #property:如果有就用值，没有就所有随机。option:如果有传值就用值，没有就随机
    HR = HttpRequest.HttpRequest()
    if(not property):
        AUTO=0
        MANUAL=1
        ISOLATED=2
        modeValue=[AUTO,MANUAL,ISOLATED]
        mode=random.choice(modeValue)
        HR.open('camera._setOptions', parameters={'property':'aaa_mode', 'value': mode})
        if(mode==MANUAL):
            propertyValue=['wb','iso_value']
        else:
            propertyValue = ['wb', 'ev_bias']
        property = random.choice(propertyValue)

    if(property=='wb'):
        if(option==None):
            option=random.randint(0,5)
    elif(property=='iso_value'):
        if(option==None):
            option=random.randint(0,9)
    elif(property=='ev_bias'):
        if (option == None):
            option = random.randint(-255, 255)

    print('p--',property,'o--',option)

    HR.open('camera._setOptions',parameters={'property':property,'value':option})
    #下次写遍历wb+iso ev+wb等等

def setOption(property=None, option=None):
    HR = HttpRequest.HttpRequest()
    HR.open('camera._setOptions', parameters={'property': property, 'value': option})

def doSetOptionRound(property=None):
    if(property=='wb'):
        for i in range(5):
            option=i
            print('p--', property, 'o--', option)
            HR = HttpRequest.HttpRequest()
            HR.open('camera._setOptions', parameters={'property': property, 'value': option})
            takePicAction(30)

def WBandEV(num,interval):
    #wb
    for value in range(num):
        # wb range is 5
        print(value % 5)
        for ev in range(-255, 256):
            setOption('ev_bias', ev)
            setOption('wb', value % 5)
            takePicAction(interval)


def WBandISO():
    #ev
    for property in range(9):
        #wb
        for option in range(14):
            doSetExposureRandom(property, option)
            TakePic(1)
            #sendTakePic()
            #print(property,option)

def TakePic(num,interval=40,random=False):
    if(random):
        doSetExposureRandom()
    for i in range(num):
        takePicAction(interval)

def TakePicCircle(num,interval=40,wb=False,evwb=True):
    if(wb):
        for value in range(num):
            #wb range is 5
            print(value % 5)
            setOption('wb',value%5)
            takePicAction(interval)
    elif(evwb):
        WBandEV(num,interval)
        for value in range(num):
            #wb range is 5
            print(value % 5)
            for ev in range(200,256):
                setOption('ev_bias',ev)
                setOption('wb', value % 5)
                takePicAction(interval)



def takePicAction(interval):
    #print('TakePic')
    logging.warning('TakePic')
    sleep(2)
    # 发送TakePicture请求
    HR = HttpRequest.HttpRequest()
    # HR.getFingerPrint()
    datalist = []
    sub_data = {"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},
                "stiching": {"mime": "jpeg",  "width": 7680,  "height": 3840,"mode": "pano"}}

    data8k3d = {"origin": {"saveOrigin": 'true', "height": 3000, "mime": "jpeg", "width": 4000}, "delay": 0, "stiching": {"mode": "3d_top_left", "height": 7680, "mime": "jpeg", "width": 7680}}
    data_burst={"stabilization": 'false',"origin": {"mime": "jpeg", "width": 4000, "bitrate": 'null',"height": 3000, "framerate": 'null', "saveOrigin": 'true'},
                "delay": 0, "burst": {"count": 10, "enable": 'true'}}

    data_8kOF={"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},"stabilization":'false',"delay":0,
                "stiching": {"algorithm":"opticalFlow","bitrate":"null","framerate":"null","mime":"jpeg","height":3840,"mode":"pano","width":7680}}

    data_8k_3d_OF = {"origin": {"mime": "jpeg", "width": 4000, "height": 3000, "saveOrigin": 'true'},
                 "stabilization": 'false', "delay": 0,
                 "stiching": {"algorithm": "opticalFlow", "bitrate": "null", "framerate": "null", "mime": "jpeg",
                              "height": 7680, "mode": "3d_top_left", "width": 7680}}

    data_raw={"origin":{"framerate":'null',"bitrate":'null',"mime":"raw","height":3000,"saveOrigin":'true',"width":4000},"stabilization":'false',"delay":0}
    data_hdr={"origin":{"framerate":'null',"bitrate":'null',"mime":"jpeg","height":3000,"saveOrigin":'true',"width":4000},
              "stabilization":'false',"delay":0,"hdr":{"min_ev":-32,"count":3,"enable":'true',"max_ev":32}}

    datalist.append(sub_data)
    datalist.append(data8k3d)
    datalist.append(data_raw)
    datalist.append(data_hdr)
    datalist.append(data_burst)
    datalist.append(data_8kOF)
    datalist.append(data_8k_3d_OF)

    origin_no_sti={"origin": {"bitrate": None, "width": 4000, "height": 3000, "mime": "jpeg", "saveOrigin": 'true', "framerate": None}}
    data = HR.open("camera._takePicture", parameters=random.choice(datalist))
    #data = HR.open("camera._takePicture", parameters=data_burst)
    logging.info(data)


    if(not data['state']=='done'):
        if (data['error']['description'] == 'camera not connected'):
            CommomUtils.Connect()
            print('reconnect ..!')
        else:
            errstr='nowtime is'+ctime()+'\ndata is:'+str(data)
            #SendEmail.send(errstr)
    sleep(interval)



def Record(sleeptime,rangenum=5,mintime=10,maxtime=15):
    for i in range(rangenum):
        startRecord()
        randomtime=random.randint(mintime,maxtime)
        print('this time random time is %s'%randomtime)
        sleep(randomtime)
        stopRecord()
        sleep(sleeptime)

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
    if(not data['state']=='done'):
        #print(type(ctime()),type(data))
        nowtime=ctime()
        datastr=str(data)
        errstr='nowtime is'+ctime()+'\ndata is:'+datastr
        #SendEmail.send(errstr)
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

    except Exception as e:
        print (e)
        secdata = HR.open("camera._stopRecording")
        # if (not data['state'] == 'done'):
        #     # print(type(ctime()),type(data))
        #     nowtime = ctime()
        #     datastr = str(data)
        #     errstr = 'nowtime is' + ctime() + '\ndata is:' + datastr
        #     print(type(nowtime), type(datastr))
        #     SendEmail.send(errstr)
        print(secdata)

def Live(runtime,sleeptime):
    for i in range(runtime):
        StartLiving()
        livetime=random.randint(10,20)
        print('this time live is',livetime)
        sleep(livetime)
        stopLive()
        sleep(sleeptime)


def getLiveExcelRow():
    file=Constant.TestCasePath
    book=xlrd.open_workbook(file)
    table=book.sheet_by_name('startlive')
    rows=table.nrows
    print(rows)
    return rows
def getLiveDataFromExcel(i):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    bg_color=xlwt.easyxf('pattern:fore_colour ocean_blue')
    table = book.sheet_by_name('startlive')
    wbook=copy(book)
    wbook.get_sheet('startlive').write(i,28,bg_color)
    wbook.save(file)


    stimime = table.cell(i, 2).value

    stiwidth = table.cell(i, 3).value

    stiheight = table.cell(i, 4).value

    stimode = table.cell(i, 5).value
    stiframerate = table.cell(i, 6).value
    stibirate = table.cell(i, 7).value
    stimap = table.cell(i, 8).value

    orimime = table.cell(i, 9).value
    oriwidth = table.cell(i, 10).value
    oriheight = table.cell(i, 11).value
    oriframerate = table.cell(i, 12).value
    oribirate = table.cell(i, 13).value
    saveori = table.cell(i, 14).value
    audmime = table.cell(i, 15).value
    audbitrate = table.cell(i, 16).value
    samplerate = table.cell(i, 17).value
    sampleformat = table.cell(i, 18).value
    channellayout = table.cell(i, 19).value
    stabilization = table.cell(i, 20).value
    liveurl = table.cell(i, 21).value
    liveonhdmi = table.cell(i, 22).value
    filesave=table.cell(i,23).value
    format=table.cell(i,24).value
    enable=table.cell(i,25).value
    interval=table.cell(i,26).value
    count=table.cell(i,27).value


    subparam = StartLive.StartLive(stimime=stimime, stiwidth=stiwidth, stiheight=stiheight,
                                   stimode=stimode, stiframerate=stiframerate, stibirate=stibirate,
                                   stimap=stimap, liveonhdmi=liveonhdmi, liveurl=liveurl,
                                   orimime=orimime, oriwidth=oriwidth, oriheight=oriheight,
                                   oriframerate=oriframerate, oribirate=oribirate,saveori=saveori,
                                   audmime=audmime, audbitraite=audbitrate, samplerate=samplerate,
                                   sampleformat=sampleformat, channellayout=channellayout,
                                   stabilization=stabilization,
                                   filesave=filesave,format=format,enable=enable,interval=interval,count=count).getJsonData()
    return subparam


def StartLiving():
    global count
    count=1
    print('startLive---')
    HR=HttpRequest.HttpRequest()
    HR.open("camera._startLive",parameters=getLiveDataFromExcel(count))
    count=count+1

def stopLive():
    HR=HttpRequest.HttpRequest()
    HR.open('camera._stopLive')
    print('stopLive--')

def PicAndRecord(sleeptime,rangenum=3,minrecord=10,maxrecord=15):
    for i in range(rangenum):
        print('pic and rec ----------PIC')
        takePicAction(sleeptime)
        print('pic and rec ----------REC')
        sleep(sleeptime)
        startRecord()
        sleep(random.randint(minrecord, maxrecord))
        stopRecord()
        sleep(sleeptime)

def Heart(sleeptime=2):
    while True:
        logging.info('Heart')
        CommomUtils.Connect()
        sleep(sleeptime)

def runThreadAs(thread1,thread2):
    #thread1 sends heart-package
    thread1.setDaemon(True)
    thread1.start()
    thread2.start()
    thread2.join()


def doStartPreview():
    HR = HttpRequest.HttpRequest()
    param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                           stiwidth='1920', stibitrate='1000',
                                           stiheight='960', stimode='pano',
                                           orimime='h265', oriframe='30',
                                           oriwidth='1920', oribitrate='15000',
                                           oriheight='1440', saveori='false').getJsonData()
    data=HR.open('camera._startPreview', parameters=param)
    print('preview----',data)
    #sleep(1)

def doConnectToCamera():
    CommomUtils.Connect()

def chooseRun(mode,runtime,sleeptime):
    tHeart = threading.Thread(target=Heart)

    if (mode == 1):
        t2Pic = threading.Thread(target=TakePic, args=(runtime,sleeptime))
        runThreadAs(tHeart, t2Pic)

    elif (mode == 2):
        t3Record = threading.Thread(target=Record, args=(runtime, 10, 12,sleeptime))
        runThreadAs(tHeart, t3Record)
    elif(mode == 3):
        tLive = threading.Thread(target=Live,args=(runtime,sleeptime))
        runThreadAs(tHeart,tLive)
    elif(mode==6):
        tPicAndRecord = threading.Thread(target=PicAndRecord(3, 10, 15,sleeptime))
        runThreadAs(tHeart, tPicAndRecord)

    elif (mode == 7):
        t2Pic = threading.Thread(target=TakePicCircle, args=(runtime,sleeptime))
        runThreadAs(tHeart, t2Pic)
def doDisconnect():
    print('\nall over %s' % ctime())
    HR = HttpRequest.HttpRequest()
    data = HR.open("camera._disconnect")
    print(data)


if __name__=='__main__':
    #n = getLiveExcelRow()
    #doConnectToCamera()
    #doStartPreview()
    #chooseRun(mode,runtimes,sleeptime)

    #chooseRun(Constant.PICANDRECORD,1,50)
    #doDisconnect()
    #WBandISO()

    doSetExposureRandom()