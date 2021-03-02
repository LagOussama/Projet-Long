import psutil

addrs = psutil.net_if_addrs()
print(addrs.keys())

from get_nic import getnic

print(getnic.interfaces())

interfaces = getnic.interfaces()
print(getnic.ipaddr(addrs.keys()))
