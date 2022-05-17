#!/bin/python3

import socket
import sys
from datetime import datetime

#DEFINE OUR TARGET

if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1]) #translating hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax python3 scanner.py <ip>")

print("-"*50)
print("SCANNING TARGET "+target)
print("TIME STARTED "  +str(datetime.now()))
print("-"*50)


try:
	for port in range(1, 65535):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port)) #returns an error indicator
		#print("Checking port {}".format(port))
		if result==0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()
except socket.gaierror:
	print("Hostaname could not be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
