#!/usr/bin/python


import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n1=raw_input("enter first number: ")
n2=raw_input("enter scnd number: ")
s.sendto(n1,("192.168.43.142",7777))
s.sendto(n2,("192.168.43.142",7777))
x=s.recvfrom(1000)
