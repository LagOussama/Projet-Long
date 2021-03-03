import psutil
import socket
import struct
import ipcalc



def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

from get_nic import getnic



class network:
	def __init__(self,cidr):
		net , mask = cidr_to_netmask(cidr)
		addr = ipcalc.IP(net, mask=mask)
		network_with_cidr = str(addr.guess_network())
		bare_network = network_with_cidr.split('/')[0]
		self.network = bare_network
		self.mask = mask
		self.hosts = None

def getInterfaces():
	addrs = psutil.net_if_addrs()
	#interfaces = getnic.interfaces()
	interfaces = getnic.ipaddr(addrs.keys())
	return interfaces

def test(states):
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



