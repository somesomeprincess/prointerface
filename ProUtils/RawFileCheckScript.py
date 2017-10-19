#encoding=utf-8
import os
from PIL import Image
import cv2

def simpleCheck(path,cphoto='',cvideo=''):

    for dirpath, dirnames, filenames in os.walk(path):
        #print('search begin!')
        #if('F:\\PIC' in dirpath or 'F:\\VID' in dirpath):
        if(cphoto):
            checkPhotoCount(path, dirpath, filenames)
        if(cvideo):
            checkVideoCount(path, dirpath, filenames)

        #checkImageCanOpen(filenames,dirpath)
        #checkRawSize(filenames, dirpath)
        checkVideoCanOpen(filenames,dirpath)
    print('search over!')


def checkVideoCount(path, dirpath, filenames):
    if (path[-1] == '\\'):
        vidpath='VID'
    else:
        vidpath='\\VID'

    if (path + vidpath in dirpath):
        filescount = len(filenames)
        #print 'dirpath------',dirpath,'\ndirnames-------------',dirnames,'\n,filenames------------',filenames,files
        #print(dirpath,filescount)
        #3d拼接或原片拼接
        if ('3d.mp4' in filenames or 'pano.mp4' in filenames and filescount != 10):
            print('common video file count not ok', dirpath)
        #timelapse没有gyro.dat
        elif(not 'gyro.dat' in filenames):
            if((filescount-1)%3!=0):
                print('timelapse file count not ok', dirpath)
        #仅原片
        elif (filescount != 9):
            print('file count not ok', dirpath)

def checkPhotoCount(path, dirpath, filenames):
    basefile=set(['origin_0.jpg','origin_1.jpg','origin_2.jpg','origin_3.jpg','origin_4.jpg','origin_5.jpg'])
    rawfile = set(['origin_0.dng', 'origin_1.dng', 'origin_2.dng', 'origin_3.dng', 'origin_4.dng', 'origin_5.dng'])
    if (path[-1] == '\\'):
        picpath='PIC'
    else:
        picpath='\\PIC'
    if (path + picpath in dirpath):
        filescount = len(filenames)
        #print(filenames)
        if(basefile.issubset(filenames) and filescount>7):
            pass
            # HDR or Burst
        elif (filescount == 19 or filescount == 61):
            pass
        #Raw
        elif(not rawfile.issubset(filenames)):
            #checkRawSize(filenames,dirpath)
            print('raw photo count not ok', dirpath)
        elif(rawfile.issubset(filenames)):
            checkRawSize(filenames,dirpath)
        else:
            print('photo count not ok', dirpath)


        #
        # elif(not 'gyro.dat' in filenames):
        #     if((filescount-1)%3!=0):
        #         print('timelapse file count not ok', dirpath)
        # elif (filescount != 9):
        #     print('file count not ok', dirpath)


def checkRawSize(filenames,dirpath):
    total=0
    kb_total=0
    for f in filenames:

        size = int(os.path.getsize(os.path.join(dirpath, f)))
        total=total+size
        kb_total=total/1024/1024
    if(kb_total!=137):
        print('raw size is not ok!!!!',dirpath)
    #print(dirpath,kb_total)



'''
paths=os.listdir(root)
for p in paths:
    if('PIC'in p):
        #print(os.path.getsize(p))
        print(p)
        for dirpath,dirnames,filenames in os.walk(root+'\\'+p):
            for f in filenames:
                #print(type(filenames))
                totalsize=os.path.getsize(os.path.join(root+'\\'+p,f))
            if(totalsize!='24000540'):
                print(p,"%s"%totalsize)
            #print(totalsize)
'''

def checkImageCanOpen(filepath,path):
    for f in filepath:
        if(f.endswith('.jpg')):
            checkimg=Image.open(path+'\\'+f).verify()
            print(checkimg)

def checkVideoCanOpen(filepath,path):
    for f in filepath:
        if(f.endswith('.mp4')):
            video=cv2.VideoCapture(path+'\\'+f)
            #print(f,video.isOpened())
            if(not video.isOpened()):
                print('video can not open!!!!', path)
                break




if __name__ == '__main__':
    #simpleCheck(r'G:\work\Pro\file\0621')
    simpleCheck("H:\\",1)