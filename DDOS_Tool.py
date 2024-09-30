from telnetlib import IP
from scapy.all import *
import signal
import sys

def signal_handler(sig, frame): 
    print('Exiting...')
    sys.exit(0) 

signal.signal(signal.SIGINT, signal_handler)  

def ping(host):
    while True: 
        sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)  
        print(f"Sent ICMP echo request to {host}") 

if __name__ == "__main__":
    target_host = "192.168.1.1"  
    ping(target_host)