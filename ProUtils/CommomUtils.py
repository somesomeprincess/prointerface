#coding:utf-8
from ProUtils import HeartBeat,HttpRequest
import xlrd
from model import StartPreviewParam,TakePicture,StartRecording,StartLive
from ProUtils import Constant
import time,threading,datetime
from multiprocessing import Process
def Connect():
    isconnect = HeartBeat.HeartBeat().IsConnect()

    if (not isconnect):
        HeartBeat.HeartBeat().IsConnect()


def ConnectWhile():
    while True:
        if (HeartBeat.HeartBeat().IsConnect()):
            break

def DisConnect():
    HR = HttpRequest.HttpRequest()
    data = HR.open("camera._disconnect")
    return data['state']=='done'

#从excel中读取用例
def StartPreviewTestCaseFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    cols = table.ncols
    ps = []
    for i in range(1, rows):
        case = table.cell(i, 0).value
        stimime = table.cell(i, 2).value
        stiframerate = table.cell(i, 3).value
        stiwidth = table.cell(i, 4).value
        stibitrate=table.cell(i, 5).value
        stiheight=table.cell(i, 6).value
        stimode = table.cell(i, 7).value
        orimime = table.cell(i, 8).value
        oriframerate = table.cell(i, 9).value
        oriwidth = table.cell(i, 10).value
        oribitrate=table.cell(i, 11).value
        oriheight=table.cell(i, 12).value
        saveorigin = table.cell(i, 13).value

        subparam = StartPreviewParam.StartPreview(stimime=stimime, stiframe=stiframerate, stiwidth=stiwidth, stibitrate=stibitrate, stiheight=stiheight, stimode=stimode,
                                                  orimime=orimime, oriframe=oriframerate, oriwidth=oriwidth, oribitrate=oribitrate, oriheight=oriheight, saveori=saveorigin).getJsonData()
        # print(case,param.getJsonData())
        ok = (case, subparam)
        ps.append(ok)
    return ps

def TakePicTestCaseFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    tab=book.sheet_by_index
    # 获取行数
    rows = table.nrows
    cols = table.ncols
    print(rows)
    ps = []
    for i in range(1, rows):
        case = table.cell(i, 0).value
        stimime = table.cell(i, 2).value

        stiwidth = table.cell(i, 3).value

        stiheight=table.cell(i, 4).value
        map=table.cell(i, 5).value
        algorithm=table.cell(i, 6).value
        stimode = table.cell(i, 7).value
        orimime = table.cell(i, 8).value

        oriwidth = table.cell(i, 9).value
        oriheight = table.cell(i, 10).value
        saveorigin = table.cell(i, 11).value
        delay=table.cell(i, 12).value
        storagepath=table.cell(i, 13).value

        subparam = TakePicture.TakePicture(stimime=stimime, stiwidth=stiwidth,  stiheight=stiheight, stimode=stimode,
                                                  orimime=orimime,  oriwidth=oriwidth,  oriheight=oriheight, saveori=saveorigin,
                                                  delay=delay,storagepath=storagepath,map=map,algorithm=algorithm).getJsonData()

        ok = (case, subparam)
        ps.append(ok)
    return ps

def StartRecordTestCaseFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    cols = table.ncols
    print(rows)
    ps=[]
    keylist = ['stimime','stiwidth','stiheight','stimode','stiframerate','stibirate','stimap','orimime','oriwidth',
               'oriheight','oriframerate','oribirate','saveorigin','audbirate','samplerate','sampleformat','channellayout','timenable','timeinterval',
               'fileoverride','storagepath','stabilization']
    valuelist=[]
    for i in range(1, rows):
        case = table.cell(i, 0).value

        stimime = table.cell(i, 2).value

        stiwidth = table.cell(i, 3).value

        stiheight=table.cell(i, 4).value

        stimode = table.cell(i, 5).value
        stiframerate=table.cell(i, 6).value
        stibirate=table.cell(i, 7).value
        stimap=table.cell(i, 8).value
        orimime =table.cell(i, 9).value

        oriwidth =table.cell(i, 10).value
        oriheight =table.cell(i, 11).value
        oriframerate = table.cell(i, 12).value
        oribirate = table.cell(i, 13).value
        saveorigin =table.cell(i, 14).value
        audmime =table.cell(i, 15).value
        audbitrate = table.cell(i, 16).value
        samplerate= table.cell(i, 17).value
        sampleformat = table.cell(i, 18).value
        channellayout= table.cell(i, 19).value
        timenable=table.cell(i, 20).value
        timeinterval=table.cell(i, 21).value
        duration=table.cell(i, 22).value
        fileoverride=table.cell(i, 23).value
        storagepath=table.cell(i, 24).value
        stabilization=table.cell(i, 25).value

        subparam = StartRecording.StartRecording(stimime=stimime, stiwidth=stiwidth,  stiheight=stiheight, stimode=stimode,stiframerate=stiframerate,stibirate=stibirate,stimap=stimap,
                                                  orimime=orimime,  oriwidth=oriwidth,  oriheight=oriheight, saveori=saveorigin,oriframerate=oriframerate,oribirate=oribirate,
                                                  audmime=audmime,audbitraite=audbitrate,samplerate=samplerate,sampleformat=sampleformat,
                                                 channellayout=channellayout,timeenable=timenable,timeinterval=timeinterval,duration=duration,fileoverride=fileoverride,
                                                 storagepath=storagepath,stabilization=stabilization).getJsonData()
        ok = (case, subparam)
        ps.append(ok)

    return ps


def StartLiveTestCaseFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    cols = table.ncols
    print(rows)
    ps = []
    for i in range(1, rows):
        case = table.cell(i, 0).value

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
        storagepath = table.cell(i, 14).value
        audmime = table.cell(i, 15).value
        audbitrate = table.cell(i, 16).value
        samplerate = table.cell(i, 17).value
        sampleformat = table.cell(i, 18).value
        channellayout = table.cell(i, 19).value
        stabilization = table.cell(i, 20).value
        liveurl = table.cell(i, 21).value
        liveonhdmi = table.cell(i, 22).value

        subparam = StartLive.StartLive(stimime=stimime, stiwidth=stiwidth, stiheight=stiheight,
                                                 stimode=stimode, stiframerate=stiframerate, stibirate=stibirate,
                                                 stimap=stimap,liveonhdmi=liveonhdmi,liveurl=liveurl,
                                                 orimime=orimime, oriwidth=oriwidth, oriheight=oriheight,
                                                  oriframerate=oriframerate, oribirate=oribirate,
                                                 audmime=audmime, audbitraite=audbitrate, samplerate=samplerate,
                                                 sampleformat=sampleformat,channellayout=channellayout,
                                                 storagepath=storagepath, stabilization=stabilization).getJsonData()
        ok = (case, subparam)
        ps.append(ok)

    return ps

def SetImageParamFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    ps = []
    for i in range(1, rows):
        case = table.cell(i, 0).value
        property = table.cell(i, 2).value
        value = table.cell(i, 3).value
        subparam=setImageParam.SetImageParam(property=property,value=value).getJsonData()
        ok = (case, subparam)
        ps.append(ok)
    return ps

def SetOptionFromExcel(sheetname):
    pass

def StichPicFileFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    ps = []
    for i in range(1, rows):
        case = table.cell(i, 0).value
        file1=table.cell(i, 2).value
        file2 = table.cell(i, 2).value
        file3 = table.cell(i, 3).value
        file4 = table.cell(i, 4).value
        file5 = table.cell(i, 5).value
        file6 = table.cell(i, 6).value

        stimime = table.cell(i, 7).value
        stiwidth = table.cell(i, 8).value
        stiheight=table.cell(i, 9).value
        stimode = table.cell(i, 10).value

        subparam = StichPicFileParam.StichPicFile(file1=file1, file2=file2, file3=file3, file4=file4, file5=file5, file6=file6,
                                                  stimime=stimime, stiwidth=stiwidth, stiheight=stiheight, stimode=stimode).getJsonData()
        # print(case,param.getJsonData())
        ok = (case, subparam)
        ps.append(ok)
    return ps

def Heart(rangetime=4,sleeptime=3):
    for i in range(rangetime):
        print('Heart',Constant.fingerprint)
        Connect()
        time.sleep(sleeptime)

def HeartThread():
    t6 = threading.Thread(target=Heart)
    t6.start()

def HeartProcess():
    p=Process(target=Heart)
    p.start()


#从excel中读取用例
def ExampleFromExcel(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    cols = table.ncols
    ps = []
    for i in range(1, rows):
        print(i)

        for j in range(1,cols):
            case = table.cell(0, j).value
            subparam=table.cell(i, j).value
            ok = (case, subparam)
            print(ok)
        ps.append(ok)
    return ps

def writeLogToFile(something):
    today = datetime.datetime.now().strftime('%Y_%m_%d_%H')
    with open(r'G:/log/' + today + '.txt', 'a') as f:
        nowtime = datetime.datetime.now().strftime('%m-%d %H:%M')
        f.write(nowtime + '----' + str(something) + '\n')

if __name__=='__main__':
    ps=StartRecordTestCaseFromExcel('startrecord')
    print(ps)