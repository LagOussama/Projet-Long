#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
import libclient
import psutil
import test1

from get_nic import getnic

#define value
def create_request(action, value):
    if action == "add":


        interfaces = test1.getInterfaces()
        ## getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        value=dict(hostname=hostname, ip_address=ip_address, interfaces=interfaces)
    if action == "search" or "add":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    else:
        return dict(
            type="binary/custom-client-binary-type",
            encoding="binary",
            content=bytes(action + value, encoding="utf-8"),
        )


class clientcmd:
    def __init__(self, host, port, action,value):
        self.sel = selectors.DefaultSelector()
        self.action = action
        self.value = value
        self.host = host
        self.port = port
    def start_connection(self, host, port, request):

        addr = (host, port)
        print("starting connection to", addr)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(self.sel, sock, addr, request)
        self.sel.register(sock, events, data=message)
    def sendCmd(self):
        request = create_request(self.action, self.value)
        self.start_connection(self.host, self.port, request)
        try:
            while True:
                events = self.sel.select(timeout=1)
                for key, mask in events:
                    message = key.data
                    try:
                        message.process_events(mask)
                    except Exception:
                        print("main: error: exception for",f"{message.addr} :\n{traceback.format_exc()}")
                        message.close()
		    # Check for a socket being monitored to continue.
                if not self.sel.get_map():
                    break

        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
    def execute(self):
        self.sendCmd()
        self.sel.close()







if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action="add"
value =""
cltCMD = clientcmd(host,port,action,value)

cltCMD.execute()