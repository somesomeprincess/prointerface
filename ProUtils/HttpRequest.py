#coding:utf-8
import urllib.request
from urllib.parse import urlencode
import json
import time
from ProUtils import Constant
from model import StartPreviewParam
import requests
class HttpRequest():
    #def open_with_requests
    def open(self,reqname,fingerprint=None,url=Constant.Common_url,**kw):
        if (fingerprint == None):
            fingerprint = Constant.fingerprint
        header = {'Fingerprint': fingerprint, 'Content-Type': 'application/json', 'User-Agent': 'Apache-HttpClient/4.4'}
        jsondata = {'name': reqname}
        jsondata.update(kw)
        #jsondata = json.dumps(jsondata)
        #request = urllib.request.Request(url, jsondata, headers=header)


        resp = requests.post(url,json=jsondata,headers=header)
        result = resp.json()

        return result

    #入参要传name,用urllib.request请求的方法
    def open_(self,reqname,fingerprint=None,url=Constant.Common_url,**kw):
        if(fingerprint==None):
            fingerprint=Constant.fingerprint
        header={'Fingerprint':fingerprint,'Content-Type':'application/json','User-Agent':'Apache-HttpClient/4.4'}
        jsondata={'name':reqname}
        jsondata.update(kw)
        jsondata=json.dumps(jsondata)
        print('1',type(jsondata))
        jsondata = urlencode(jsondata).encode('UTF-8')

        request=urllib.request.Request(url,jsondata,headers=header)
        print(type(jsondata))

        resp=urllib.request.urlopen(request,timeout=10)
        result=resp.read()
        data=json.loads(result)
        return data

    #入参不用传name
    def openCommon(self,param,fingerprint,url=Constant.Common_url):
        header={'Fingerprint':Constant.fingerprint,'Content-Type':'application/json','User-Agent':'Apache-HttpClient/4.4'}
        jsondata=json.dumps(param)
        request=urllib.request.Request(url,jsondata,headers=header)
        resp=urllib.request.urlopen(request,timeout=5)
        result=resp.read()
        data=json.loads(result)
        return data


    def openHeart_(self,url=Constant.Heart_url,**kw):
        #header={'Fingerprint':Constant.fingerprint,'Content-Type':'application/json'}
        header = {'Fingerprint': Constant.fingerprint, 'Content-Type': 'application/json',
                  'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5, application/x-mpegURL',
                  'x-flash-version':'22,0,0,175','User-Agent':'Apache-HttpClient/4.4'}

        jsondata = json.dumps(kw)
        request=urllib.request.Request(url,jsondata,headers=header)

        resp=urllib.request.urlopen(request)
        result=resp.read()
        data=json.loads(result)
        return data

    def openHeart(self,url=Constant.Heart_url,**kw):
        header = {'Fingerprint': Constant.fingerprint, 'Content-Type': 'application/json',
                  'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5, application/x-mpegURL',
                  'x-flash-version':'22,0,0,175','User-Agent':'Apache-HttpClient/4.4'}
        resp=requests.post(url,json=kw,headers=header)
        result=resp.json()
        return result


    def getFingerPrint(self):
        data=self.open('camera._connect')
        print('getFingerPrint ---:%s'%data)
        if(data):
            if(data['state']=='done'):
                print(data['results']['Fingerprint'])
                Constant.fingerprint=data['results']['Fingerprint']
            elif(data['error']['description']==u'already connected by another'):
                self.open("camera._disconnect")
                time.sleep(10)
                return False
            else:
                time.sleep(10)
                print('sleep')
                self.getFingerPrint()
            return True
        else:
            print('get fringerprint failed!!')
            return False
        #self.fingerprint=data['results']['error']





if __name__ == '__main__':
    req=HttpRequest()
    para=StartPreviewParam.StartPreview(stimime='h265').getJsonData()
    data=req.open_with_requests('camera._startPreview',parameters=para)
    print(data)


