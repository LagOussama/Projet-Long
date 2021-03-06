import psutil
from get_nic import getnic
import time
from threading import Thread
from Csniffer import *
import asyncio

def snifferThread(interfaceName,host,port):
    print ("--I'm scanning %s :D " % interfaceName)
    getPacketInfo(interfaceName,host,port)



def Main(host,port):
    #dict shows complete info of all the host interfaces (state, @ip, @mac, ...)
    addrs = psutil.net_if_addrs()
    interfInfo  = getnic.ipaddr(addrs)
    asyncio.set_event_loop(None)
    loop = asyncio.new_event_loop()
    asyncio.get_child_watcher().attach_loop(loop)

    print(interfInfo)

    for key in list(interfInfo.keys()):
        if(interfInfo[key]['state'] == 'UP'):
            myThread = Thread(target=snifferThread, args=(key,host,port,))
            try:
                myThread.start()
            except Exception as err:
                pass # or raise err

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)
  host, port = sys.argv[1], int(sys.argv[2])
  Main(host,port)
