import os
import logging
import time
class WriteLog(object):
    logdir='./log/'
    def __init__(self,loggername=''):
        self.loggername=loggername
        datefmt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.runtime_path=''.join([self.logdir,datefmt,'Runtime.log'])
        self.error_path=''.join([self.logdir,datefmt,'Error.log'])

        # self.runtime_path = ''.join([datefmt, 'Runtime.log'])
        # self.error_path = ''.join([datefmt, 'Error.log'])




    def add_logger(self):
        #创建一个logging
        logger=logging.getLogger('')
        logger.setLevel(logging.INFO)
        # logging.basicConfig(level=logging.DEBUG,
        #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                     datefmt='%a, %d %b %Y %H:%M:%S',
        #                     filemode='w')
        if(not logger.handlers):
            fhder=logging.FileHandler(self.runtime_path)
            fhder.setLevel(logging.INFO)
            fhder1=logging.FileHandler(self.error_path)
            fhder1.setLevel(logging.ERROR)
            #create formatter
            fmt='%(asctime)s [%(name)s-%(levelname)s]:%(message)s'
            datefmt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            formatter=logging.Formatter(fmt,datefmt)

            fhder.setFormatter(formatter)
            fhder1.setFormatter(formatter)
            logger.addHandler(fhder)
            logger.addHandler(fhder1)
        return logger



    def blogger(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s [%(name)s-%(levelname)s]:%(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=self.runtime_path,
                            filemode='a')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(name)-2s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
if __name__ == '__main__':
    WriteLog().blogger()
    logging.info('This is info message')
    logging.debug('This is warning message')
    datefmt = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    print(datefmt)
    try:
        print(5/0)
    except Exception as e:
        logging.error(e)


