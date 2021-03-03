from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['NetworkTraffic']

def insertPacketInfo(packetDict, commande):
    if(commande == "ip_layer"):
        coll = db['packetIP']
        coll.insert_one(packetDict)
    elif(commande == "dns_layer"):
        coll = db['packetDNS']
        coll.insert_one(packetDict)
    elif(commande == " transport_layer"):
        coll = db['packetTCUDP']
        coll.insert_one(packetDict)
    else:
        print(" invalid commande!")

def insertNetwork(netDic):
    coll = db['Networks']
    coll.insert_one(netDic)

def insertHost(hostDic):
    coll = db['Hosts']
    coll.insert_one(hostDic)

def insertInterfaces(interDic):
    coll = db['Interfaces']
    coll.insert_one(interDic)

def isNetworkExist(Network, mask):
    coll = db['Networks']
    res = coll.find({'network':Network, 'mask':mask})
    if (len(list(res))>0):
        return True
    return False
