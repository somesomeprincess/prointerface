import random
import copy
def xunhuan(num):

    for i in range(num):

        print('wb--------------',i%5)
        for ev in range(-255,255):
            print('ev--',ev)

def lam():
    a=list(map(lambda x: x, range(7, 44)))
    print(a)

def chou():
    propertyValue = ['wb', 'iso_value', 'shutter_value']
    print(len(propertyValue))
    print(random.choices(propertyValue))
    print(random.sample(propertyValue,random.randint(1,len(propertyValue))))
def ran():
    for i in range(10):
        print(random.randint(0,2))
def size():
    propertyValue = ['wb', 'iso_value', 'shutter_value']

def copi():
    base_data = {
        "audio": {"bitrate": 128, "mime": "aac", "samplerate": 48000, "sampleFormat": "s16", "channelLayout": "stereo"},
        "origin": {"mime": "h264", "framerate": 30, "width": 3200, "bitrate": 40960, "height": 2400,
                   "saveOrigin": 'true'}}
    sti_3840_1920 = {"width": 3840, "mime": "h264", "height": 1920, "mode": "pano", "framerate": 30, "bitrate": 40960}
    sub_data4k3d = copy.deepcopy(base_data)
    sub_data4k3d['origin']['framerate']=40
    print('origin-------',sub_data4k3d['origin'])
    print(base_data)
    print(st)
def ranfloat():
    for i in range(10):
        n=random.uniform(1,10)
        print(n,round(n,1))

def bianliang():

    global a
    a=''
    print(type(a))
if __name__ == '__main__':
    bianliang()