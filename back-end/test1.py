import psutil
import socket
import struct
import ipcalc

addrs = psutil.net_if_addrs()
print(addrs.keys())

def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

from get_nic import getnic





print(getnic.interfaces())
interfaces = getnic.interfaces()
states = getnic.ipaddr(addrs.keys())
for key in states:
	if states[key]['state'] == 'UP':
		print(states[key])
		if 'inet4' in states[key]:
			print(states[key]['inet4'])
			net , mask = cidr_to_netmask(states[key]['inet4'])
			print(net)
			print(mask)
			addr = ipcalc.IP(net, mask=mask)
			network_with_cidr = str(addr.guess_network())
			bare_network = network_with_cidr.split('/')[0]
			print(bare_network)
			#print(states[key]['inet4'].split('/'))



