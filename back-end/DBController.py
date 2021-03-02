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
