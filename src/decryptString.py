from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import PKCS1_OAEP
from configReader import configReader
import logging.config
import base64

conReader = configReader()
logFileName = conReader.getLogFileName()
logging.config.fileConfig(logFileName, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
priKeyFile = conReader.getPrivateKeyFile()

class decryptString():
    def __init__(self,encodedString):
        self.encodedString = encodedString
        byteEncodedString = bytes(self.encodedString, encoding="ASCII")
        try:
            private_key_string = open(priKeyFile,"r").read()
            logger.info("Opened Private Key File.")
            
            private_key = RSA.importKey(private_key_string)
            logger.info("Turned it into a key.")
            
            base64Decrypted = base64.b64decode(byteEncodedString)
            oaep = PKCS1_OAEP.new(private_key, SHA256)
            decrypted = oaep.decrypt(base64Decrypted)
            logger.info("Decrypted string.")
            self.decryptedString = decrypted.decode("utf-8") 
            
        except:
            logger.error("Failed to decrypt string!")    