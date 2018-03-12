from script.PicRecordScriptNoLog import *
from log import writelog
#设置相机ip?
writelog.WriteLog().blogger()
doConnectToCamera()
doStartPreview()
#chooseRun(mode,runtimes,sleeptime),
chooseRun(Constant.TAKEPICTURE, 2000, 20)
doDisconnect()