import DBController as db


class Connexion:
    def __init__(self, ip1, ip2):
        self.ip1 = ip1
        self.ip2 = ip2
        self.last_update = None
        self.nbr_packets = 1
    def equals(self,ip1,ip2):
    	if ip1 == self.ip1 and ip2 == self.ip2 :
    		return True
    	return False
    def addpackt(self):
    	self.nbr_packets += 1
    def _to_dict(self):
    	return dict(ip1=self.ip1, ip2 =self.ip2 , last_update = self.last_update, nbr_packets= self.nbr_packets)



def return_IndexCon_ifexist(cons,ip1,ip2):
	i = 0
	for con in cons:
		if con.equals(ip1,ip2) :
			return i
		i+=1
	return -1

def CreatConnexions():
	# get hosts 
	# for each hots take all connexions  ! host1 ! host2 
	# 	if connexion exist skip
	hosts = db.getHosts()
	for host in hosts:
		ipv4host = db.getip4interfaces(host['hostname'])
		#print(ipv4host)
		for ip_cidr in ipv4host:
			ip_add= ip_cidr.split("/")[0]
			packets = db.gethostpackets(ip_add)
			cons = []
			#print(packets)
			for p in packets:
				ipdest = p['ipDestination']
				#print("true") if db.conexist(ip_add,ipdest) else print("false")
				if (not db.conexist(ip_add,ipdest)) : 
					#update if already exist else create connextion
					index = return_IndexCon_ifexist(cons,ip_add,ipdest)
					if index == -1 :
						con = Connexion(ip_add,ipdest)
						cons.append(con)
					else :
						cons[index].addpackt()
			#print(cons)
			Connextions = []
			for con in cons:
				Connextions.append(con._to_dict())
			db.insertCons(Connextions)

CreatConnexions()
