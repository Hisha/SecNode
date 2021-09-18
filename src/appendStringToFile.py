from configReader import configReader
import logging.config

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class appendStringToFile():
    def __init__(self,fileName,appendString):
        self.fileName = fileName
        self.appendString = appendString
        
        appendFile = open(self.fileName,"a")
        logger.info("%s opened to append.", self.fileName)
        appendFile.write(self.appendString + "\n")
        logger.info("Appended %s", self.fileName)
        appendFile.close()
        logger.info("%s closed.", self.fileName)