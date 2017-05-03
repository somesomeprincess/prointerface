#coding:utf-8
from ProUtils import HeartBeat,HttpRequest
import xlrd
from model import StartPreviewParam,TakePicture,setImageParam,StichPicFileParam,StartRecording
from ProUtils import Constant
import time,threading
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
    ps = []
    for i in range(1, rows):
        case = table.cell(i, 0).value
        stimime = table.cell(i, 2).value

        stiwidth = table.cell(i, 3).value

        stiheight=table.cell(i, 4).value

        stimode = table.cell(i, 5).value
        orimime = table.cell(i, 6).value

        oriwidth = table.cell(i, 7).value
        oriheight = table.cell(i, 8).value
        saveorigin = table.cell(i, 9).value
        audmime = table.cell(i, 10).value
        audbitrate = table.cell(i, 11).value
        samplerate= table.cell(i, 12).value

        sampleformat = table.cell(i, 13).value
        channellayout= table.cell(i, 14).value
        stiframerate= table.cell(i, 15).value
        subparam = StartRecording.StartRecording(stimime=stimime, stiwidth=stiwidth,  stiheight=stiheight, stimode=stimode,
                                                 stiframerate=stiframerate,
                                                  orimime=orimime,  oriwidth=oriwidth,  oriheight=oriheight, saveori=saveorigin,
                                                  audmime=audmime,audbitraite=audbitrate,samplerate=samplerate,sampleformat=sampleformat,
                                                 channellayout=channellayout).getJsonData()
        print(subparam)
        ok = (case, subparam)
        ps.append(ok)
    return ps


def StartLiveTestCaseFromExcel(sheetname):
    pass

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

def Heart():
    for i in range(4):
        print('Heart')
        Connect()
        time.sleep(3)

def HeartThread():
    t6 = threading.Thread(target=Heart)
    # t6 = Process(target=sendHeart)
    t6.start()
    t6.join()

if __name__=='__main__':
    ps=StartPreviewTestCaseFromExcel('startPreview')
    print(ps)