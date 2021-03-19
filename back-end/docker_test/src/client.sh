#!/bin/sh
python3 appclient.py $1 15000& 
python3 sniffingHost.py
