import psutil
from get_nic import getnic
import time
from threading import Thread
from sniffer import *

def snifferThread(interfaceName):
    print ("--I'm scanning %s :D " % interfaceName)
    getPacketInfo(interfaceName)

def Main():
    #dict shows complete info of all the host interfaces (state, @ip, @mac, ...)
    addrs = psutil.net_if_addrs()
    interfInfo  = getnic.ipaddr(addrs)
    
    for key in list(interfInfo.keys()):
        myThread = Thread(target=snifferThread, args=(key,))
        myThread.start()
      
if __name__ == "__main__":
  Main()

