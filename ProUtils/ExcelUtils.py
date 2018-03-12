import xlrd,xlutils,xlwt
from ProUtils import Constant
from model import StartRecording
from  xlutils import copy
class ExcelUtils():
    def __init__(self,sheetname,startrow,startcol):
        self.book=xlrd.open_workbook(Constant.TestCasePath)
        self.sheet=self.book.sheet_by_name(sheetname)
        self.nRows=self.sheet.nrows
        self.curRow=startrow
        self.startcol=startcol


    def next(self):
        #valuelist = []
        if(self.has_next()):

            # bg_color=xlwt.easyxf('pattern:fore_colour ocean_blue')
            # nt=xlutils.copy.copy()
            tem = []
            for col in range(2, 26):
                cell = self.sheet.cell(self.curRow, col)
                cvalue=cell.value
                ctype=cell.ctype
                if(ctype==2 and cvalue%1==0):
                    cvalue=int(cvalue)
                tem.append(cvalue)
            #valuelist.append(tem)
            subparam = StartRecording.StartRecording(*tem).getJsonData()
        self.curRow=self.curRow+1
        return subparam

    def has_next(self):
        if(self.curRow>=self.nRows or self.nRows==0):
            return False
        else:
            return True

    def StartRecordTestCaseFromExcelNew(sheetname):
        file = Constant.TestCasePath
        book = xlrd.open_workbook(file,formatting_info=True)
        table = book.sheet_by_name(sheetname)
        # 获取行数
        rows = table.nrows
        valuelist = []
        # bg_color=xlwt.easyxf('pattern:fore_colour ocean_blue')
        # nt=xlutils.copy.copy()
        for row in range(3, rows):
            tem = []
            for col in range(2, 26):
                onevalue = table.cell(row, col).value
                tem.append(onevalue)
            valuelist.append(tem)
            subparam = StartRecording.StartRecording(*tem).getJsonData()
        # subparam = StartRecording.StartRecording(*valuelist[0]).getJsonData()
        print(len(valuelist))
        # print('\n----',subparam)

    def addColor(self):
        bg_color = xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;')
        wbook = copy.copy(self.book)
        wbook.get_sheet('record').write(self.curRow, self.startcol, style=bg_color)
        wbook.save(Constant.TestCasePath)

if __name__ == '__main__':
    e=ExcelUtils()
    while(e.has_next()):
        print(e.next())
        print(e.curRow)
        e.addColor()