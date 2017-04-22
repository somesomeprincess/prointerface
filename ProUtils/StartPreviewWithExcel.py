#coding:utf-8
import xlrd
from model import StartPreviewParam
import unittest
from parameterized import parameterized
from CommomUtils import StartPreviewTestCaseFromExcel,TakePicTestCaseFromExcel


class Nose(unittest.TestCase):

    @parameterized.expand(TakePicTestCaseFromExcel('takePicture_normal'))
    def testA(self,a,b):
        print(a,b)
