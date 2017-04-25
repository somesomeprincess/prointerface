#coding:utf-8
#data不包含name的
class TakePicture():
    name = "camera._takePicture"
    def __init__(self,stimime,stiwidth,stiheight,stimode,map,algorithm,
                 orimime,oriwidth,oriheight,saveori,delay,storagepath,**kw):

        self.stimime=stimime
        self.map=map
        self.stiwidth=stiwidth
        self.algorithm=algorithm
        self.stiheight=stiheight
        self.stimode=stimode
        self.orimime=orimime
        self.oriwidth=oriwidth
        self.delay=delay
        self.storagepath=storagepath
        self.oriheitht=oriheight
        self.saveori=saveori
        if(stimime and stiwidth and stiheight and stimode):
            if (map and algorithm):
                self.data = {
                    "stiching": {"mime": self.stimime, "width": self.stiwidth,
                                 "height": self.stiheight, "mode": self.stimode, "map": map, "algorithm": algorithm},
                    "origin": {"mime": self.orimime, "width": self.oriwidth,
                               "height": self.oriheitht, "saveOrigin": self.saveori}}
            else:
                self.data = {
                    "stiching": {"mime": self.stimime, "width": self.stiwidth,
                                 "height": self.stiheight, "mode": self.stimode},
                    "origin": {"mime": self.orimime, "width": self.oriwidth,
                               "height": self.oriheitht, "saveOrigin": self.saveori}}
        else:
            self.data = {"origin": {"mime": self.orimime, "width": self.oriwidth,"height": self.oriheitht, "saveOrigin": self.saveori}}



        for key, value in kw.items():
            if (key not in self.data['parameters']):
                self.data['parameters'][key] = value

    def getJsonData(self):
        return self.data

if __name__=='__main__':
    a=None
    if(a):
        print('true')