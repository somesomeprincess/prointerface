import os
def picfile_name(dir):
    gen='/mnt/media_rw/2253-1DC7/'
    picdic={}
    list=[]
    uuid=405
    for root in os.listdir(dir):
        if(root.startswith('PIC_2017_11_13_18')):
            parameters={}
            tem=gen+root
            #list.append(tem)
            parameters['uuid']=str(uuid)
            parameters['input']={'path':tem}
            parameters['blend'] = {"mode":"pano"}
            parameters['gyro'] ={"enable":1}
            parameters['output']={'file':tem+'/h.jpg'}
            parameters['output']['image']={"width":7680,"height":3840}
            #parameters['output']['audio'] ={"type":"pano"}
            if(len(list)<13):
                list.append(parameters)
            else:
                break

            uuid=uuid+1
    picdic['name']="stitcher.add_task"
    picdic['parameters']=list
    return picdic

video='"width":7680,"height":3840'
def recfile_name(dir):
    gen='/mnt/media_rw/579B-8F8B/'
    picdic={}
    list=[]
    uuid=405
    for root in os.listdir(dir):
        if(root.startswith('VID_2017_11_13_20')):
            parameters={}
            tem=gen+root
            #list.append(tem)
            parameters['uuid']=str(uuid)
            parameters['input']={'path':tem}
            parameters['blend'] = {"mode":"pano","calibration":{"captureTime":10}}
            parameters['gyro'] ={"enable":1}
            parameters['output']={'file':tem+'/b.mp4'}
            parameters['output']['video']={"width":5120,"height":2560}
            parameters['output']['video']['bitrate']=50000
            parameters['output']['video']['fps'] = 30
            parameters['output']['audio'] ={"type":"pano"}
            if(len(list)<10):
                list.append(parameters)
            else:
                break

            uuid=uuid+1
    picdic['name']="stitcher.add_task"
    picdic['parameters']=list
    return picdic



def recOnefile_name(dir):
    gen='/mnt/media_rw/579B-8F8B/'
    picdic={}
    list=[]
    uuid=560
    for root in os.listdir(dir):
        if(root.startswith('VID_2017_11_14_19')):
            for i in range(50000,90000,10000):
                parameters={}
                tem=gen+root
                #list.append(tem)
                parameters['uuid']=str(uuid)
                parameters['input']={'path':tem}
                parameters['blend'] = {"mode":"pano","calibration":{"captureTime":10}}
                parameters['gyro'] ={"enable":1}
                parameters['output']={'file':tem+'/'+str(i)+'threed.mp4'}
                parameters['output']['video']={"width":3840,"height":3840}
                parameters['output']['video']['bitrate']=i
                parameters['output']['video']['fps'] = 30
                parameters['output']['audio'] ={"type":"pano"}
                if(len(list)<10):
                    list.append(parameters)
                else:
                    break

                uuid=uuid+1
    picdic['name']="stitcher.add_task"
    picdic['parameters']=list
    return picdic


def recOnefileNoDisk_name():
    tem='/mnt/media_rw/F085-0C4A/VID_2017_11_16_16_47_03'
    picdic={}
    list=[]
    uuid=603
    for i in range(50000,90000,10000):
        parameters={}

        #list.append(tem)
        parameters['uuid']=str(uuid)
        parameters['input']={'path':tem}
        parameters['blend'] = {"mode":"pano","calibration":{"captureTime":10}}
        parameters['gyro'] ={"enable":1}
        parameters['output']={'file':tem+'/'+str(i)+'new.mp4'}
        parameters['output']['video']={"width":5120,"height":2560}
        parameters['output']['video']['bitrate']=i
        parameters['output']['video']['fps'] = 30
        parameters['output']['audio'] ={"type":"pano"}
        if(len(list)<10):
            list.append(parameters)
        else:
            break

        uuid=uuid+1
    picdic['name']="stitcher.add_task"
    picdic['parameters']=list
    return picdic
if __name__ == '__main__':
    #print('/mnt/media_rw/FF10-EE7B/')
    #print(picfile_name('H:\\'))
    result=recOnefileNoDisk_name()
    result=str(result).replace('\'','\"')
    print(result)