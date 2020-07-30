# ARP-Spoofing

The task is to write a Python 3 program that makes use of scapy to implement IP spoofing against a TCP server listening on a machine. 
The implementation involves the spoofing from a virtual machine running under VirtualBox on the same host as the TCP server. 
The spoofing attack will cause the victim machine to believe it has an established connection with an arbitrary IP address of the attacker's choosing.

The implementation involves the usage of ARP cache poisoning method to poison the cache table of the machine to implement a man in the middle attack.

The code is a python implementation using the built in IP and TCP libraries.
The three way handshake involves the client to send the ACK+1 number to the server to succesffuly initiate the connection.
The python code calculates the sequence number of the ACK to be sent to the server inside a spoofed packet to fool the server into thinking that the packet is coming from the client.
