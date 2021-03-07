from pymongo import MongoClient

#client = MongoClient('192.168.1.7', 27017)
client = MongoClient('mongodb://admin:myadminpassword@172.17.0.1:27017')
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


def getHosts():
    coll = db['Hosts']
    return coll.find()


def getip4interfaces(hostname):
    host_interfaces = getinterfaces(hostname)
    ip4addreses = []
    for interface in host_interfaces:
        interface = getInterface_info(interface,hostname)
        if 'inet4' in interface:
            ip4addreses.append(interface['inet4'])
    return ip4addreses

def getinterfaces(hostname):
    coll = db['Hosts']
    return list(coll.find_one({'hostname': hostname})['interfaces'])

def getInterface_info(interface,hostname):
    coll = db['Interfaces']
    return coll.find_one({'Hostname': hostname,'HostInterfaceName':interface})


def gethostpackets(hostip):
    coll = db['packetIP']
    #print(hostip)
    query = {'ipSource': hostip} #x2
    results = list(coll.find(query))
    query = {'ipDestination': hostip}
    results+=(list(coll.find(query)))
    return results

#gethostpackets('192.168.1.7')
def conexist(ip1,ip2):
    coll = db['Connexions']
    res = coll.find({'ip1':ip1, 'ip2':ip2})
    if (len(list(res))>0):
        return True

    res = coll.find({'ip1':ip2, 'ip2':ip1})
    if (len(list(res))>0):
        return True

    return False
def insertCons(Cons):
   for con in Cons:
        insertCon(con)

def insertCon(con):
    coll = db['Connexions']
    coll.insert_one(con)

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
