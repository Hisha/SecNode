#import socket
from getExtIP import getExtIP
from keysCheckCreate import keysCheckCreate

keysCheckCreate()

try:
    serverIP = getExtIP()
    print("External IP : ", serverIP.ip)
except:
    print("No internet access found.")


#serverPort = 13122

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(('0.0.0.0', serverPort))
