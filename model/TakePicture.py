#coding:utf-8
#data不包含name的
class TakePicture():
    name = "camera._takePicture"
    def __init__(self,stimime=None,stiwidth=None,stiheight=None,stimode=None,map=None,algorithm=None,
                 orimime=None,oriwidth=None,oriheight=None,saveori=None,delay=None,storagepath=None,**kw):

        if(stimime and stiwidth and stiheight and stimode):
            if (map and algorithm):
                self.data = {
                    "stiching": {"mime": stimime, "width": stiwidth,
                                 "height": stiheight, "mode": stimode, "map": map, "algorithm": algorithm},
                    "origin": {"mime": orimime, "width": oriwidth,
                               "height": oriheight, "saveOrigin": saveori}}
            else:
                self.data = {
                    "stiching": {"mime": stimime, "width": stiwidth,
                                 "height": stiheight, "mode": stimode},
                    "origin": {"mime": orimime, "width": oriwidth,
                               "height": oriheight, "saveOrigin": saveori}}
        else:
            self.data = {"origin": {"mime": orimime, "width": oriwidth,"height": oriheight, "saveOrigin": saveori}}

        if(delay):
            self.data['delay']=delay
        if(storagepath):
            self.data['storagepath']=storagepath


        for key, value in kw.items():
            if (key not in self.data.keys()):
                self.data[key] = value

    def getJsonData(self):
        return self.data

if __name__=='__main__':
    a=None
    if(a):
        print('true')