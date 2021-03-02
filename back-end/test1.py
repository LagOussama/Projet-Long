import psutil
from get_nic import getnic

addrs = psutil.net_if_addrs()
interfaces = getnic.interfaces()
print(getnic.ipaddr(addrs))
