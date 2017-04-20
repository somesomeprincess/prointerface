#coding:utf-8
import xlrd
from model import StartPreviewParam
import unittest
from parameterized import parameterized

class Excel():
    def readCase(self):
        file = r'G:\work\Pro\startpreview.xlsx'
        book = xlrd.open_workbook(file)
        table = book.sheet_by_index(0)
        # 获取行数
        rows = table.nrows
        cols = table.ncols
        # print(rows)
        ps = []
        for i in range(1, rows):
            yuanzu = ()
            '''
            for k in range(2,cols):
                print(table.cell(i, k).value)
            '''

            case = table.cell(i, 0).value
            #print(case)
            stimime = table.cell(i, 2).value
            stiframerate = table.cell(i, 3).value
            stiwidth = table.cell(i, 4).value
            subparam = StartPreviewParam.StartPreviewParam(stimime=stimime, stiframe=stiframerate, stiwidth=stiwidth).getJsonData()
            # print(case,param.getJsonData())
            ok = (case, subparam)
            ps.append(ok)
        return ps

    def readCaseTest(self):
        file = r'G:\work\Pro\startpreview.xlsx'
        book = xlrd.open_workbook(file)
        table = book.sheet_by_index(0)
        # 获取行数
        rows = table.nrows
        cols = table.ncols
        # print(rows)
        ps = []
        for i in range(1, rows):
            yuanzu = ()




            case = table.cell(i, 0).value
            #print(case)
            for k in range(2,cols):

                print(i,k)

                print(table.cell(i,k))
                print('\n')
            stimime = table.cell(i, 2).value
            stiframerate = table.cell(i, 3).value
            stiwidth = table.cell(i, 4).value
            subparam = StartPreviewParam.StartPreviewParam(stimime=stimime, stiframe=stiframerate, stiwidth=stiwidth).getJsonData()
            # print(case,param.getJsonData())
            ok = (case, subparam)
            ps.append(ok)
        return ps

if __name__=='__main__':
    data=Excel().readCaseTest()
    # print(data)
    # print(type(data))
