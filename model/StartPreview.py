import json
class StartPreviewParam():
    name = "camera._startPreview"
    def __init__(self,stimime="h264",stiframe=30,stiwidth=1920,
                 stibitrate=1000,stiheight=960,stimode="pano",orimime='h264',oriframe=30,oriwidth=1920,
                 oribitrate=15000,oriheight=1440,saveori='false',**kw):

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

        self.data = "parameters": {
            "stiching": {"mime": self.stimime, "framerate": self.stiframe, "width": self.stiwidth,
                         "bitrate": self.stibitrate, "height": self.stiheight, "mode": self.stimode},
            "origin": {"mime": self.orimime, "framerate": self.oriframe, "width": self.oriwidth,
                       "bitrate": self.oribitrate, "height": self.oriheitht,
                       "saveOrigin": self.saveori}}

        for key, value in kw.items():
            if (key not in self.data['parameters']):
                self.data['parameters'][key] = value


        #print(self.data)

    def getJsonData(self):
        return self.data

if __name__=='__main__':
    s=StartPreviewParam(stimime='h265')