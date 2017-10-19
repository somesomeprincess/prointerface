from ProUtils import HttpRequest
from ProUtils import Constant

class HeartBeat():

    def IsConnect(self):
        HR=HttpRequest.HttpRequest()
        if(not Constant.fingerprint):
            HR.getFingerPrint()
        if(Constant.fingerprint):
            data=HR.openHeart(key=0)
            self.returndata=data
            if(data):
                if('error' not in data):
                    return True
                else:
                    print(data['error'])
                    # if(data['error']['description']==u'camera not connected'):
                    #     Constant.fingerprint=None
                    return False
        return False

    def getHeartData(self):
        return self.returndata

if __name__=='__main__':
    h=HeartBeat()
    if(not h.IsConnect()):
        print(h.IsConnect())