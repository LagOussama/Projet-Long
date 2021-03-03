import psutil

addrs = psutil.net_if_addrs()
print(addrs.keys())

from get_nic import getnic

print(getnic.interfaces())

interfaces = getnic.interfaces()
states = getnic.ipaddr(addrs.keys())
for key in states:
	if states[key]['state'] == 'UP':
		print(states[key])
		if 'inet4' in states[key]:
			print(states[key]['inet4'])



