def takePicAction(interval):
    #print('TakePic')
    logging.warning('TakePic')
    sleep(2)
    # 发送TakePicture请求
    global HR
    if (not HR):
        HR = HttpRequest.HttpRequest()

    datalist = []
    sub_data = {"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},
                "stiching": {"mime": "jpeg",  "width": 7680,  "height": 3840,"mode": "pano"}}

    data8k3d = {"origin": {"saveOrigin": 'true', "height": 3000, "mime": "jpeg", "width": 4000}, "delay": 0, "stiching": {"mode": "3d_top_left", "height": 7680, "mime": "jpeg", "width": 7680}}
    data_burst={"stabilization": 'false',"origin": {"mime": "jpeg", "width": 4000, "bitrate": 'null',"height": 3000, "framerate": 'null', "saveOrigin": 'true'},
                "delay": 0, "burst": {"count": 10, "enable": 'true'}}

    data_8kOF={"origin": {"mime": "jpeg",  "width": 4000,  "height": 3000,"saveOrigin": 'true'},"stabilization":'false',"delay":0,
                "stiching": {"algorithm":"opticalFlow","bitrate":"null","framerate":"null","mime":"jpeg","height":3840,"mode":"pano","width":7680}}

    data_8k_3d_OF = {"origin": {"mime": "jpeg", "width": 4000, "height": 3000, "saveOrigin": 'true'},
                 "stabilization": 'false', "delay": 0,
                 "stiching": {"algorithm": "opticalFlow", "bitrate": "null", "framerate": "null", "mime": "jpeg",
                              "height": 7680, "mode": "3d_top_left", "width": 7680}}

    data_raw={"origin":{"framerate":'null',"bitrate":'null',"mime":"raw","height":3000,"saveOrigin":'true',"width":4000},"stabilization":'false',"delay":0}
    data_hdr={"origin":{"framerate":'null',"bitrate":'null',"mime":"jpeg","height":3000,"saveOrigin":'true',"width":4000},
              "stabilization":'false',"delay":0,"hdr":{"min_ev":-32,"count":3,"enable":'true',"max_ev":32}}

    datalist.append(sub_data)
    datalist.append(data8k3d)
    datalist.append(data_raw)
    datalist.append(data_hdr)
    datalist.append(data_burst)
    datalist.append(data_8kOF)
    datalist.append(data_8k_3d_OF)

    origin_no_sti={"origin": {"bitrate": None, "width": 4000, "height": 3000, "mime": "jpeg", "saveOrigin": 'true', "framerate": None}}
    ranreq=random.choice(datalist)
    if(ranreq[0]=='hdr'):
        pass
    data = HR.open("camera._takePicture", parameters=random.choice(datalist))
    #data = HR.open("camera._takePicture", parameters=data_burst)
    logging.info(data)


    if(not data['state']=='done'):
        if (data['error']['description'] == 'camera not connected'):
            CommomUtils.Connect()
            logging.info('reconnect ..!')

        else:
            errstr='nowtime is'+ctime()+'\ndata is:'+str(data)
            #SendEmail.send(errstr)
    sleep(interval)

