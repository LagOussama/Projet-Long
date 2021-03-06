import DBController as db
import socket
import time
import datetime
import os
import sys
     

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

#CreatConnexions()


LOG_FNAME = "network.log"
FILE = os.path.join(os.getcwd(), LOG_FNAME)

#by default test internet connexion to the addresse 1.1.1.1 port 53
def send_ping_request(host="1.1.1.1", port=53, timeout=3):
	try:
	    socket.setdefaulttimeout(timeout)
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    s.connect((host,port))
	except OSError as error:
	    return False
	else:
	    s.close()
	    return True
def write_permission_check():
    try:
        with open(FILE, "a") as file:
            pass
    except OSError as error:
        print("Log file creation failed")
        sys.exit()
    finally:
        pass
def calculate_time(start, stop):
    time_difference = stop - start
    seconds = float(str(time_difference.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]
def my_net_connection(host="1.1.1.1", port=53, timeout=3,ping_freq=2):
    monitor_start_time = datetime.datetime.now()
    motd = "Network connection monitoring started at: " + str(monitor_start_time).split(".")[0] + " Sending ping request in " + str(ping_freq) + " seconds"
    print(motd)
 
    with open(FILE, "a") as file:
        file.write("\n")
        file.write(motd + "\n")
    while True:
        if send_ping_request():
            time.sleep(ping_freq)
        else:
            down_time = datetime.datetime.now()
            fail_msg = "Network Connection Unavailable at: " + str(down_time).split(".")[0]
            print(fail_msg)
            with open(FILE, "a") as file:
                file.write(fail_msg + "\n")
                i = 0
            while not send_ping_request(host, port, timeout):
                time.sleep(1)
                i += 1
                if i >= 3600:
                    i = 0
                    now = datetime.datetime.now()
                    continous_message = "Network Unavailabilty Persistent at: " + str(now).split(".")[0]
                    print(continous_message)
                    with open(FILE, "a") as file:
                        file.write(continous_message + "\n")
            up_time = datetime.datetime.now()
            uptime_message = "Network Connectivity Restored at: " + str(up_time).split(".")[0]
 
            down_time = calculate_time(down_time, up_time)
            _m = "Network Connection was Unavailable for " + down_time
 
            print(uptime_message)
            print(_m)
 
            with open(FILE, "a") as file:
                file.write(uptime_message + "\n")
                file.write(_m + "\n")
my_net_connection()