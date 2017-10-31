import xlwt,xlrd
from ProUtils import Constant
from xlutils.copy import copy

#测了就打橙色
def workbookForColor():
    file = Constant.TestCasePath
    book = xlrd.open_workbook(file)
    pattern=xlwt.Pattern()
    pattern.pattern_fore_colour=5
    style=xlwt.XFStyle()
    style.pattern=pattern
    bg_color = xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;')
    table = book.sheet_by_name('startlive')
    wbook = copy(book)
    wsheet=wbook.get_sheet('startlive')
    wsheet.write(6, 28, style=bg_color)


    wbook.save(file)


def long(*args):
    print(args)

