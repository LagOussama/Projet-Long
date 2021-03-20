#!/bin/sh
python3 ./serverfiles/appserver.py 0.0.0.0 15000 & 
python3 ./common/sniffer_app.py #&
#python3 ./serverfiles/sniffingHost.py
