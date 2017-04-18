from ProUtils import HttpRequest
from ProUtils import Constant

class HeartBeat():

    def IsConnect(self):
        HR=HttpRequest.HttpRequest()
        if(not Constant.fingerprint):
            HR.getFingerPrint()
        if(Constant.fingerprint):
            data=HR.openHeart(key=0)
            if(data):
                if(not data.has_key('error')):
                    return True
                else:
                    print(data['error'])
                    return False
        return False

if __name__=='__main__':
    h=HeartBeat()
    if(not h.IsConnect()):
        print(h.IsConnect())