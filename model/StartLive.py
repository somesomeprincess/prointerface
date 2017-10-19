#coding:utf-8
#data不包含name的
class StartLive():
    name = "camera._start"
    def __init__(self,stimime=None,stiwidth=None,stiheight=None,stimode=None,stiframerate=None,stibirate=None,stimap=None,
                 liveurl=None,filesave=None,liveonhdmi=None,format=None,
                 orimime=None,  oriwidth=None,  oriheight=None, saveori=None,oriframerate=None,oribirate=None,
                 audmime=None,audbitraite=None,samplerate=None,sampleformat=None,
                 channellayout=None,enable=None,interval=None,
                 count=None,stabilization=None,**kw):

        self.data =  {"audio": {"channelLayout": channellayout, "bitrate": audbitraite, "samplerate": samplerate,"mime": audmime, "sampleFormat": sampleformat},
                      "origin": {"mime": orimime,  "width": oriwidth,"height": oriheight,"saveOrigin": saveori,"bitrate":oribirate,"framerate":oriframerate}}
        self.data['stiching']= {"mime": stimime, "width": stiwidth, "height": stiheight, "mode": stimode,"framerate":stiframerate,"bitrate":stibirate,"map":stimap,
                                "_liveUrl":liveurl,"fileSave":filesave,"liveOnHdmi":liveonhdmi,"format":format}
        if (stabilization):
            self.data['stabilization'] = stabilization
        self.data['autoConnect']={"enable":enable,"interval":interval,"count":count}

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
    s=StartRecording(stimime='h265')