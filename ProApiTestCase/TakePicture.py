#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant
from ProUtils import HeartBeat

class TakePicture(unittest.TestCase):
    def atestTakePicture(self):
        isconnect = HeartBeat.HeartBeat().IsConnect()
        if (not isconnect):
            HeartBeat.HeartBeat().IsConnect()

        HR=HttpRequest.HttpRequest()
        HR.getFingerPrint()
        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=sub_data)
        self.assertIsNotNone(data,u'data为空！%s'%data)
        self.assertTrue(data['state']=='done','state不等于done')
        id=data['results']['id']
        self.assertIsNotNone(id,'id等于空')
        while True:
            data = HR.openHeart()
            idRes = data['state']['idRes']
            if(idRes):
                self.assertEqual(idRes,id)
                break

