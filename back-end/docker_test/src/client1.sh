#!/bin/sh
python3 ./clientfiles/appclient.py 172.30.200.10  15000 #& 
python3 ./clientfiles/sniffingHost.py 172.30.200.10  15000
