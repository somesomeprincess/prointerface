#coding:utf-8
#data不包含name的
class StartPreview():
    name = "camera._startPreview"
    def __init__(self,stimime,stiframe,stiwidth,
                 stibitrate,stiheight,stimode,orimime,oriframe,oriwidth,
                 oribitrate,oriheight,saveori,**kw):

        self.stimime=stimime
        self.stiframe=stiframe
        self.stiwidth=stiwidth
        self.stibitrate=stibitrate
        self.stiheight=stiheight
        self.stimode=stimode
        self.orimime=orimime
        self.oriframe=oriframe
        self.oriwidth=oriwidth
        self.oribitrate=oribitrate
        self.oriheitht=oriheight
        self.saveori=saveori

        self.data =  {
            "stiching": {"mime": self.stimime, "framerate": self.stiframe, "width": self.stiwidth,
                         "bitrate": self.stibitrate, "height": self.stiheight, "mode": self.stimode},
            "origin": {"mime": self.orimime, "framerate": self.oriframe, "width": self.oriwidth,
                       "bitrate": self.oribitrate, "height": self.oriheitht,
                       "saveOrigin": self.saveori}}

        for key, value in kw.items():
            if (key not in self.data['parameters']):
                self.data['parameters'][key] = value


        print(self.data)

    def getJsonData(self):
        return self.data

if __name__=='__main__':
    s=StartPreview(stimime='h265')