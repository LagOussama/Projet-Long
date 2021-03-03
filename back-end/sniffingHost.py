import psutil
from get_nic import getnic
import time
from threading import Thread

addrs = psutil.net_if_addrs()
interfInfo  = getnic.ipaddr(addrs)

for elt in interfInfo.keys():
    print(interfInfo[elt]['state'])
    


