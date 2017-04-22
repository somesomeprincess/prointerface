#coding:utf-8
from ProUtils import HttpRequest
import unittest
from ProUtils import Constant,CommomUtils
from ProUtils import HeartBeat
import threading
from time import sleep

class TakePicture(unittest.TestCase):
    def testTakePicture(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()

        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=sub_data)
        print(data)
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'done', 'state不等于done')
        id = data['results']['id']
        self.assertIsNotNone(id, 'id等于空')

        # 等待心跳包返回id
        '''
        while True:
            heartdata = HR.openHeart()
            idRes = heartdata['state']['idRes']
            if (idRes):
                self.assertEqual(idRes, id)
                break
        '''





        '''
        #根据心跳包返回的id请求getResult获取结果
        param=dict(list_ids=idRes)

        result_data = HR.open("camera._getResult", parameters=param)
        state=result_data['state']
        self.assertIsNotNone(state)
        self.assertTrue(state=='done','_getResult的state不等于done！state: %s'%state)
        '''

    def AddToThread(self):
        t1 = threading.Thread(target=TakePicture.TakePic)
        t2 = threading.Thread(target=TakePicture.Heart)

        t1.setDaemon(True)
        t2.setDaemon(True)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def Heart(self):
        while True:
            print('Heart')
            CommomUtils.Connect()
            sleep(3)


    def TakePic(self):
        CommomUtils.Connect()
        HR=HttpRequest.HttpRequest()

        sub_data={"origin":{"mime":"jpeg","framerate":None,"width":4000,"bitrate":None,"height":3000,"saveOrigin":'true'},
                  "stiching":{"mime":"jpeg","framerate":None,"width":7680,"bitrate":None,"height":3840,"mode":"pano"}}
        data=HR.open("camera._takePicture",parameters=sub_data)
        self.assertIsNotNone(data, u'data为空！%s' % data)
        self.assertTrue(data['state'] == 'done', 'state不等于done')
        id = data['results']['id']
        self.assertIsNotNone(id, 'id等于空')
        sleep(10)

