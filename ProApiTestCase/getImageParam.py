from ProUtils import HttpRequest
import unittest

class GetImageParam(unittest.TestCase):
    def atestGetImageParam(self):
        HR=HttpRequest.HttpRequest()
        HR.getFingerPrint()
        data=HR.open("camera._getImageParam")
        print(data)