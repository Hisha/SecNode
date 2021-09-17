#import socket
from getExtIP import getExtIP
from keysCheckCreate import keysCheckCreate

keysCheckCreate()

serverIP = getExtIP()

print("External IP : ", serverIP.ip)

#serverPort = 13122

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(('0.0.0.0', serverPort))
