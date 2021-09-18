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
pubKeyFile = conReader.getPublicKeyFile()

class encryptString():
    def __init__(self,rawString):
        self.rawString = rawString
        try:
            public_key_string = open(pubKeyFile,"r").read()
            logger.info("Opened Public Key File.")
            
            public_key = RSA.importKey(public_key_string)
            logger.info("Turned it into a key.")
            
            oaep = PKCS1_OAEP.new(public_key, SHA256)
            encrypted = oaep.encrypt(bytes(self.rawString, encoding="ASCII"))
            b64cipher = base64.b64encode(encrypted)
            logger.info("Encrypted string.")
            self.encryptedString = b64cipher.decode("utf-8")    
            
        except:
            logger.error("Failed to encrypt string!")
            
       
          
                