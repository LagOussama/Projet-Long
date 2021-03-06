import psutil
from get_nic import getnic
import time
from threading import Thread
from sniffer import *
import asyncio

def snifferThread(interfaceName):
    print ("--I'm scanning %s :D " % interfaceName)
    getPacketInfo(interfaceName)



def Main():
    #dict shows complete info of all the host interfaces (state, @ip, @mac, ...)
    addrs = psutil.net_if_addrs()
    interfInfo  = getnic.ipaddr(addrs)
    asyncio.set_event_loop(None)
    loop = asyncio.new_event_loop()
    asyncio.get_child_watcher().attach_loop(loop)
    for key in list(interfInfo.keys()):
        if(interfInfo[key]['state'] == 'UP'):
            myThread = Thread(target=snifferThread, args=(key,))
            try:
                myThread.start()
            except Exception as err: 
                pass # or raise err

if __name__ == "__main__":
  Main()



