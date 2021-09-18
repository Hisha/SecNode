from configReader import configReader
from keysCheckCreate import keysCheckCreate
from peerFileCheckCreate import peerFileCheckCreate

import logging.config

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

keysCheckCreate()
peerFileCheckCreate()



