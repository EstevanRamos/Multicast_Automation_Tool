import os
import subprocess
from rich import print
	
def list_devices():
	#ip link show
	command = ["ip", "link", "show" ]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	print(process.stdout.read()+ "\n")
	
def enable_mc(interface):
	#sudo ip link set multicast on dev eth0
	command = ["ip", "link", "set" , "multicast", "on" , "dev", interface ]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	
	command = ["ip", "link", "show" , interface]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	print(process.stdout.read())
	
def disable_mc(interface):
	#sudo ip link set multicast off dev eth0
	command = ["ip", "link", "set" , "multicast", "off" , "dev", interface ]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	
	command = ["ip", "link", "show" , interface]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	print(process.stdout.read())

def enable_linux():
	#sysctl -w net.ipv4.icmp_echo_ignore_broadcasts = 0
	#in some versions of linux, linux will block MC traffic
	command = ["sysctl", "-w",  "net.ipv4.icmp_echo_ignore_broadcasts=0"]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	print(process.stdout.read())
	
def disable_linux():
	#sysctl -w net.ipv4.icmp_echo_ignore_broadcasts = 0
	command = ["sysctl", "-w",  "net.ipv4.icmp_echo_ignore_broadcasts=1"]
	process = subprocess.Popen(command, stdout = subprocess.PIPE, universal_newlines=True)
	print(process.stdout.read())
	
def test_mc_traffic():
	#iperf -s -u -B 224.1.1.1 -i 1 SERVER
	#iperf -c 224.1.1.1 -u -T 32 -t 3 -i 1 client
	listener = ["iperf" ,"-s","-u","-B" ,"224.1.1.1" ,"-i" ,"1"]
	sender = ["iperf","-c","224.1.1.1","-u","-T","32","-t","3","-i","1"]
	
	print("creating server:")
	print()
	server = subprocess.Popen(listener, stdout = subprocess.PIPE, universal_newlines=True)
	client = subprocess.Popen(sender )
	polls = 0
	
	while server.poll() is None:
	    if polls == 12:
	    	print(l)
	    	break
	    
	    l = server.stdout.readline() # This blocks until it receives newline.	
	    polls += 1
	    print(l)
	 
	server.kill()
	client.kill()
