#coding:utf-8
import random
import threading
from time import ctime, sleep
from ProUtils import CommomUtils, SendEmail,Constant,HttpRequest


from model import StartPreviewParam
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

def runThreadAs(thread1,thread2):
    #thread1 sends heart-package
    thread1.setDaemon(True)
    thread1.start()
    thread2.start()
    thread2.join()

def doStartPreview():
    pass

def doConnectToCamera():
    CommomUtils.Connect()

def chooseRun(mode,runtime,sleeptime):
    t5 = threading.Thread(target=sendPicAndRecord)
    t6 = threading.Thread(target=sendHeart)
    tRecord = threading.Thread(target=sendRecord)
    if(mode == 4):
        runThreadAs(t6, t5)
    elif(mode==5):
        runThreadAs(t6, tRecord)

def doDisconnect():
    print('\nall over %s' % ctime())
    HR = HttpRequest.HttpRequest()
    data = HR.open("camera._disconnect")
    print(data)


if __name__=='__main__':
    doConnectToCamera()
    doStartPreview()
    #chooseRun(mode,runtimes,sleeptime)
    chooseRun(Constant.TAKERECORD,100,40)
    doDisconnect()

