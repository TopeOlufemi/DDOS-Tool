from telnetlib import IP
from scapy.all import *
import signal
import sys
import logging

logging.basicConfig(filename='ping_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def signal_handler(sig, frame): 
    print('Exiting...')
    sys.exit(0) 

signal.signal(signal.SIGINT, signal_handler)  

def ping(host):
    while True: 
        sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)  
        log_message = f"Sent ICMP echo request to {host}"
        print(log_message)
        logging.info(log_message) 
if __name__ == "__main__":
    
    target_host = input("Enter the target host: ")
     
    ping(target_host)
