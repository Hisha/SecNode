import json

class configReader():
    def __init__(self):
        with open('config.json') as f:
            parsed = json.load(f)
            self.logFileName = parsed['logFileName']
            self.rsaKeySize = parsed['rsaKeySize']
            self.privateKeyFile = parsed['privateKeyFile']
            self.publicKeyFile = parsed['publicKeyFile']
            self.peerFileName = parsed['peerFileName']
            self.serverPort = parsed['serverPort']
        
    def getLogFileName(self):
        return self.logFileName   
    
    def getRSAKeySize(self):
        return self.rsaKeySize
    
    def getPrivateKeyFile(self):
        return self.privateKeyFile
    
    def getPublicKeyFile(self):
        return self.publicKeyFile
    
    def getPeerFileName(self):
        return self.peerFileName
    
    def getServerPort(self):
        return self.serverPort