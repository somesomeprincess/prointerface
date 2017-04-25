#coding:utf-8
from ProUtils import HttpRequest
from ProUtils import Constant,CommomUtils
import unittest
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')

class QueryState(unittest.TestCase):
    def testQueryState_ok(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()
        data=HR.open("camera._queryState")
        self.assertIsNotNone(data['state'],'获取state失败！')
        self.assertTrue(data['state']=='done','state不等于done！')
        self.assertTrue(data.has_key('results'),'没有results关键字！')
        results=data['results']
        self.assertIsNotNone(results,'获取results失败！')
        preview=results['preview']
        self.assertIsNotNone(preview['width'],'获取width失败！')


