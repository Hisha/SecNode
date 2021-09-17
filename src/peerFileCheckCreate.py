from os.path import exists
from configReader import configReader
import logging.config

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

peerFileName = conReader.getPeerFileName()

class peerFileCheckCreate():
    def __init__(self):
        peerFileCheckCreate.checkExists(self)
        
    def checkExists(self):
        if exists(peerFileName):
            logger.warning("Peer file exists.")
            return True
        else:
            peerFileCheckCreate.createPeerFile(self)
            
    def createPeerFile(self):    
        logger.info("Generating peer file...")
        f= open(peerFileName,"w")
        f.close()
        logger.info("Peer file created.")