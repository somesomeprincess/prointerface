#coding:utf-8
#data不包含name的
class StartPreview():
    name = "camera._startPreview"
    def __init__(self,stimime=None,stiframe=None,stiwidth=None,
                 stibitrate=None,stiheight=None,stimode=None,orimime=None,oriframe=None,oriwidth=None,
                 oribitrate=None,oriheight=None,saveori=None,**kw):

        self.data =  {
            "stiching": {"mime": stimime, "framerate": stiframe, "width": stiwidth,
                         "bitrate": stibitrate, "height": stiheight, "mode": stimode},
            "origin": {"mime": orimime, "framerate": oriframe, "width": oriwidth,
                       "bitrate": oribitrate, "height": oriheight,
                       "saveOrigin": saveori}}

        for key, value in kw.items():
            '''
            if (key not in self.data['parameters']):
                self.data['parameters'][key] = value
            '''
            if (key not in self.data.keys()):
                self.data[key] = value

    def getJsonData(self):
        return self.data

if __name__=='__main__':
    s=StartPreview(stimime='h265')