import xlrd,xlwt
from ProUtils import Constant
from model import StartRecording
import xlutils
from script import *
def StartRecordTestCaseFromExcelNew(sheetname):
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    table = book.sheet_by_name(sheetname)
    # 获取行数
    rows = table.nrows
    valuelist=[]
    #bg_color=xlwt.easyxf('pattern:fore_colour ocean_blue')
    #nt=xlutils.copy.copy()
    for row in range(3,rows):
        tem = []
        for col in range(2,26):

            onevalue=table.cell(row,col).value
            tem.append(onevalue)
        valuelist.append(tem)
        subparam=StartRecording.StartRecording(*tem).getJsonData()
    #subparam = StartRecording.StartRecording(*valuelist[0]).getJsonData()
    print(len(valuelist))
    #print('\n----',subparam)

if __name__ == '__main__':
    ps = StartRecordTestCaseFromExcelNew('record')
    print(ps)