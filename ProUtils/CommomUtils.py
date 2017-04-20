from ProUtils import HeartBeat


def Connect():
    isconnect = HeartBeat.HeartBeat().IsConnect()
    if (not isconnect):
        HeartBeat.HeartBeat().IsConnect()


def ConnectWhile():
    while True:
        if (HeartBeat.HeartBeat().IsConnect()):
            break
