#!/usr/bin/python
#encoding:utf-8
import xlrd

def ad():
    print('a')

class CreateExcel:
    def __init__(self,filepath,sheetname,url,beginindex=7,para_begin_col=3,argtotal=10):
        #参数最多10个
        #定义全局变量
        global argscount,requestMethod,reqHeader
        #打开excel
        print(filepath,sheetname)
        print('init testframe')
        try:
            book=xlrd.open_workbook(filepath)
            sheet=book.sheet_by_name(sheetname)
            argscount = sheet.cell(2, 2)
        except:
            print('open fail')

        self.url=url
        self.beginindex=beginindex
        self.para_begin_col=para_begin_col
        self.argtotal=argtotal




    def a(self):
        print('a')