from pymongo import MongoClient
import appclient
#client = MongoClient('192.168.1.7', 27017)
#client = MongoClient('mongodb://admin:myadminpassword@172.17.0.1:27017')
#client = MongoClient('mongodb://172.35.200.10:27017')
#db = client['NetworkTraffic']


class clientserverDbcontroller:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def insertPacketInfo(self, packetDict, commande):
        action = "insertPacketInfo"
        value  = dict(packetDict=packetDict,commande=commande)
        cltCMD = appclient.clientcmd(self.host,self.port,action,value)
        cltCMD.execute()

        return False
    def insertCons(self, Cons):
        action = "insertCons"
        value  = dict(Cons=Cons)
        cltCMD = appclient.clientcmd(self.host,self.port,action,value)
        cltCMD.execute()

    def insertCon(self, con):
        action = "insertCon"
        value  = dict(con=con)
        cltCMD = appclient.clientcmd(self.host,self.port,action,value)
        cltCMD.execute()

    def insertNetwork(self, netDic):
        action = "insertNetwork"
        value  = dict(netDic=netDic)
        cltCMD = appclient.clientcmd(self.host,self.port,action,value)
        cltCMD.execute()
    def insertHost(self, hostDic):
        action = "insertHost"
        value  = dict(hostDic=hostDic)
        cltCMD = appclient.clientcmd(self.host,self.port,action,value)
        cltCMD.execute()

    def insertInterfaces(self, interDic):
        action = "insertInterfaces"
        value  = dict(interDic=interDic)
        cltCMD = appclient.clientcmd(self.host,self.port,action,value)
        cltCMD.execute()
