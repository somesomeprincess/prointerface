from .PicRecordScriptNoLog import *
def doSetPropertyRandom(property=None, option=None):
    #property:如果有就用值，没有就所有随机。option:如果有传值就用值，没有就随机

    if(not property):
        modeValue=['brightness','saturation','sharpness','contrast']
        mode=random.choice(modeValue)


        properties=random.sample(modeValue, random.randint(1, len(modeValue)))
        for property in range(len(properties)):

            if (mode == 'brightness'):
                value = random.randint(-255, 255)
            elif (mode == 'saturation' or mode == 'contrast'):
                value = random.randint(0, 255)
            elif (mode == 'sharpness'):
                value = random.randint(3, 6)
            global HR
            HR.open('camera._setOptions', parameters={'property': modeValue, 'value': mode})
            sleep(2)
    else:
        HR.open('camera._setOptions', parameters={'property': property, 'value': option})
