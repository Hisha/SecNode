from Cryptodome.PublicKey import RSA
from os.path import exists
from configReader import configReader
import logging.config

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

keySize = conReader.getRSAKeySize()
priKeyFile = conReader.getPrivateKeyFile()
pubKeyFile = conReader.getPublicKeyFile()

class keysCheckCreate():
    def __init__(self):
        keysCheckCreate.checkKeys(self)
        
    def checkKeys(self):
        if exists(priKeyFile) and exists(pubKeyFile):
            logger.warning("Keys Exists.")
            return True
        else:
            keysCheckCreate.createKeys(self)
        
    def createKeys(self):
        logger.info("Generating %s RSA keys...", keySize)
        key = RSA.generate(keySize)
        logger.info("%s RSA keys generated.", keySize)
        logger.info("Private key exporting...")
        private_key = key.export_key()
        file_out = open(priKeyFile, "wb")
        file_out.write(private_key)
        file_out.close()
        logger.info("Private key exported.")
        logger.info("Public key exporting...")
        public_key = key.publickey().export_key()
        file_out = open(pubKeyFile, "wb")
        file_out.write(public_key)
        file_out.close()
        logger.info("Public key exported.")
        return True
        