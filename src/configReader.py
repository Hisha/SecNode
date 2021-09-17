import json

class configReader():
    def __init__(self):
        with open('config.json') as f:
            parsed = json.load(f)
            self.logFileName = parsed['logFileName']
            self.rsaKeySize = parsed['rsaKeySize']
            self.privateKeyFile = parsed['privateKeyFile']
            self.publicKeyFile = parsed['publicKeyFile']
        
    def getLogFileName(self):
        return self.logFileName   
    
    def getRSAKeySize(self):
        return self.rsaKeySize
    
    def getPrivateKeyFile(self):
        return self.privateKeyFile
    
    def getPublicKeyFile(self):
        return self.publicKeyFile