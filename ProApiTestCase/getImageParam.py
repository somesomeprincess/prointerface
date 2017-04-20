from ProUtils import HttpRequest
import unittest
@unittest.skip()
class GetImageParam(unittest.TestCase):
    def testGetImageParam(self):
        HR=HttpRequest.HttpRequest()
        HR.getFingerPrint()
        data=HR.open("camera._getImageParam")
        print(data)