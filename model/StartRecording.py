#coding:utf-8
#data不包含name的
class StartRecording():
    name = "camera._startPreview"
    def __init__(self,stimime=None,stiwidth=None,stiheight=None,stimode=None,stiframerate=None,stibirate=None,stimap=None,
                 orimime=None,  oriwidth=None,  oriheight=None, saveori=None,oriframerate=None,oribirate=None,
                 audmime=None,audbitraite=None,samplerate=None,sampleformat=None,
                 channellayout=None,timeenable=None,timeinterval=None,duration=None,fileoverride=None,
                 storagepath=None,stabilization=None,**kw):

        self.data =  {"audio": {"channelLayout": channellayout, "bitrate": audbitraite, "samplerate": samplerate,"mime": audmime, "sampleFormat": sampleformat},
                      "origin": {"mime": orimime,  "width": oriwidth,"height": oriheight,"saveOrigin": saveori,"bitrate":oribirate,"framerate":oriframerate}}
        if(stimime and stiwidth and stiheight and stimode and stiframerate and stibirate):
            self.data['stiching']= {"mime": stimime, "width": stiwidth, "height": stiheight, "mode": stimode,"framerate":stiframerate,"bitrate":stibirate,"map":stimap}
        if(timeenable and timeinterval):
            self.data['timelapse']={"enable":timeenable, "interval":timeinterval}
        if(duration):
            self.data['duration']=duration
        if (fileoverride):
            self.data['fileOverride'] = fileoverride
        if (storagepath):
            self.data['storagePath'] = storagepath
        if (stabilization):
            self.data['stabilization'] = stabilization

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