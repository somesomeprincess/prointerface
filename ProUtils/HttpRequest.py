import urllib2
import json
import time
from ProUtils import Constant
from model import StartPreviewParam
class HttpRequest():


    def open(self,reqname,url=Constant.Common_url,**kw):
        header={'Fingerprint':Constant.fingerprint,'Content-Type':'application/json','User-Agent':'Apache-HttpClient/4.4'}
        jsondata={'name':reqname}
        jsondata.update(kw)
        jsondata=json.dumps(jsondata)

        request=urllib2.Request(url,jsondata,headers=header)

        resp=urllib2.urlopen(request,timeout=5)
        result=resp.read()
        data=json.loads(result)
        return data

    def openCommon(self,param,url=Constant.Common_url):
        header={'Fingerprint':Constant.fingerprint,'Content-Type':'application/json','User-Agent':'Apache-HttpClient/4.4'}
        jsondata=param
        jsondata=json.dumps(jsondata)

        request=urllib2.Request(url,jsondata,headers=header)

        resp=urllib2.urlopen(request,timeout=5)
        result=resp.read()
        data=json.loads(result)
        return data


    def openHeart(self,url=Constant.Heart_url,**kw):
        #header={'Fingerprint':Constant.fingerprint,'Content-Type':'application/json'}
        header = {'Fingerprint': Constant.fingerprint, 'Content-Type': 'application/json',
                  'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5, application/x-mpegURL',
                  'x-flash-version':'22,0,0,175','User-Agent':'Apache-HttpClient/4.4'}

        #jsondata=kw
        #jsondata=json.dumps(jsondata)
        jsondata = json.dumps(kw)
        request=urllib2.Request(url,jsondata,headers=header)

        resp=urllib2.urlopen(request,timeout=5)
        result=resp.read()
        data=json.loads(result)
        return data


    def getFingerPrint(self):
        data=self.open('camera._connect')
        print('getFingerPrint ---:%s'%data)
        if(data):
            if(data['state']=='done'):
                print(data['results']['Fingerprint'])
                Constant.fingerprint=data['results']['Fingerprint']
            else:
                time.sleep(10)
                print('sleep')
                self.getFingerPrint()
            return True
        else:
            print('get fringerprint failed!!')
            return False
        #self.fingerprint=data['results']['error']


'''
    class Builder():
        requrl=None
        data=None
        def setFingerPrint(self,fingerprint):
            Constant.fingerprint=fingerprint
        def setUrl(self,url):
            self.requrl=url
        def setData(self,data):
            self.data=data

        def buildRequest(self):
            return HttpRequest()

'''





if __name__ == '__main__':
    req=HttpRequest()
    para=StartPreviewParam.StartPreviewParam(stimime='h265').getJsonData()
    data=req.open('camera._startPreview',parameters=para)
    print(data)


