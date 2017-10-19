import smtplib
from email.mime.text import MIMEText
from email.header import Header

from ProUtils import CommomUtils, HttpRequest,Constant
from model import StartPreviewParam
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf8')
def send(errmessage):
    msg=MIMEText(errmessage,'plain',_charset='utf-8')
    msg['From']='l6114@qq.com'
    msg['To']='l6114@qq.com'
    msg['Subject']=Header('camera abnormal..'+Constant.ip,'utf-8')
    qqusrname='l6114@qq.com'
    usrname='l6114@qq.com'
    qqpwd='bcxkgzqlswhocbaa'

    smtpobj = smtplib.SMTP('smtp.qq.com', 587)
    smtpobj.starttls()
    # smtpobj = smtplib.SMTP('localhost')
    smtpobj.set_debuglevel(1)
    # smtpobj.sendmail('l6114@qq.com','l6114@qq.com',msg.as_string())
    smtpobj.login(qqusrname, qqpwd)
    smtpobj.sendmail(usrname, usrname, msg.as_string())
    smtpobj.quit()


if __name__=='__main__':
    CommomUtils.Connect()
    HR = HttpRequest.HttpRequest()
    param = StartPreviewParam.StartPreview(stimime='h264', stiframe='30',
                                           stiwidth='1920', stibitrate='1000',
                                           stiheight='960', stimode='pano',
                                           orimime='h265', oriframe='30',
                                           oriwidth='1920', oribitrate='15000',
                                           oriheight='1440', saveori='false').getJsonData()
    preivewdata = HR.open('camera._startPreview', parameters=param)
    if(not preivewdata['state']=='done'):
        send(preivewdata+"")
    send('err')
