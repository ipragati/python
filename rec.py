#!/usr/bin/python


import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",7777))
n1=s.recvfrom(1000)
n2=s.recvfrom(1000)
print int(n1[0])+int(n2[0])
x=raw_input("enter something :")
s.sendto(x,n1[1])


