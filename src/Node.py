from configReader import configReader
from getExtIP import getExtIP
from keysCheckCreate import keysCheckCreate
from peerFileCheckCreate import peerFileCheckCreate
from encryptString import encryptString
#import socket
import logging.config
from decryptString import decryptString

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

keysCheckCreate()
peerFileCheckCreate()

try:
    serverIP = getExtIP()
    logger.info("Received external IP address %s", serverIP.ip)
        
except:
    logger.error("No internet access found.") 

try:
    encrytIPAddy = encryptString(serverIP.ip)
    encryptedIPAddy = encrytIPAddy.encryptedString   
    logger.info("Encrypted IP: %s", encryptedIPAddy)
     
except:
    logger.error("Tried but failed to encrypt for some reason.")
    
try:
    decryptIPAddy = decryptString(encryptedIPAddy)
    decryptedIPAddy = decryptIPAddy.decryptedString
    logger.info("Decrypted IP: %s", decryptedIPAddy)

except:
    logger.error("Tried but failed to decrypt for some reason.")

#serverPort = 13122

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(('0.0.0.0', serverPort))
