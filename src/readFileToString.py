from configReader import configReader
import logging.config

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class readFileToString():
    def __init__(self,fileName):
        self.fileName = fileName
        
        readFile = open(self.fileName,"r")
        logger.info("%s opened to read.", self.fileName)
        readLine = readFile.read().replace("\n", "")
        logger.info("Read line from %s.", self.fileName)
        readFile.close()
        logger.info("%s closed.", self.fileName)
        self.readString = readLine
        