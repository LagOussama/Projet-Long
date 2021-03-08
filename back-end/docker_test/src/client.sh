#!/bin/sh
python3 appclient.py websniff 15000& 
python3 sniffingHost.py
