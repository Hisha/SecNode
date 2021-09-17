from configReader import configReader
from getExtIP import getExtIP
from keysCheckCreate import keysCheckCreate
#import socket
import logging.config

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

keysCheckCreate()

try:
    serverIP = getExtIP()
    logger.info("External IP : %s", serverIP.ip)
except:
    logger.error("No internet access found.")


#serverPort = 13122

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(('0.0.0.0', serverPort))
