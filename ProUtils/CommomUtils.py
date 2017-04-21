#coding:utf-8
from ProUtils import HeartBeat
import xlrd
from model import StartPreviewParam
from ProUtils import Constant

def Connect():
    isconnect = HeartBeat.HeartBeat().IsConnect()
    if (not isconnect):
        HeartBeat.HeartBeat().IsConnect()


def ConnectWhile():
    while True:
        if (HeartBeat.HeartBeat().IsConnect()):
            break

#从excel中读取用例
def StartPreviewTestCaseFromExcel(sheetname):
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

        subparam = StartPreviewParam.StartPreviewParam(stimime=stimime, stiframe=stiframerate,stiwidth=stiwidth,stibitrate=stibitrate,stiheight=stiheight,stimode=stimode,
                                                       orimime=orimime,oriframe=oriframerate,oriwidth=oriwidth,oribitrate=oribitrate,oriheight=oriheight,saveori=saveorigin).getJsonData()
        # print(case,param.getJsonData())
        ok = (case, subparam)
        ps.append(ok)
    return ps

def TakePicTestCaseFromExcel(sheetname):
    pass

def StartRecordTestCaseFromExcel(sheetname):
    pass

def StartLiveTestCaseFromExcel(sheetname):
    pass