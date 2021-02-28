import pyshark
import time
import json
from pymongo import MongoClient


def getPacketInfo(networkInterface=None):
    if networkInterface is None:
        raise Exception("Please specify an interface.")
    else:
        print("listening on %s" % networkInterface)
        capture = pyshark.LiveCapture(interface=networkInterface)
        for packet in capture.sniff_continuously(packet_count=70):
            try:

                localtime = time.asctime(time.localtime(time.time()))  
                protocol = packet.transport_layer
                src_addr = packet.ip.src   
                src_port = packet[protocol].srcport 
                dst_addr = packet.ip.dst            
                dst_port = packet[protocol].dstport 
                pkt_id   = packet.ip.id
                pkt_len  = packet.ip.len
                pkt_ttl  = packet.ip.ttl

                pktInfo = {
                    "time" : localtime,
                    "protocolType" : protocol,
                    "ipSource" :src_addr,
                    "portSource" : src_port,
                    "ipDestination": dst_addr,
                    "portDestination" : dst_port,
                    "identification" : pkt_id,
                    "packetLength": pkt_len,
                    "packetTimeToLive" : pkt_ttl
                }

                sniffToDb(pktInfo)

            except AttributeError as e:
                pass


def sniffToDb(packetDict):
    client = MongoClient('localhost', 27017)
    db = client['NetworkTraffic']
    pakcetDocument = db['packetIP']
    pakcetDocument.insert_one(packetDict)
getPacketInfo("wlp3s0")