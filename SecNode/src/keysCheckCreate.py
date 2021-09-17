from Crypto.PublicKey import RSA
from os.path import exists

keySize = 4096
priKeyFile = "private.pem"
pubKeyFile = "public.pem"

class keysCheckCreate():
    def __init__(self):
        keysCheckCreate.checkKeys(self)
                  
        
    def checkKeys(self):
        if exists(priKeyFile) and exists(pubKeyFile):
            print("Keys Exists.")
            return True
        else:
            keysCheckCreate.createKeys(self)
            
        
    def createKeys(self):
        print("Generating", keySize, "RSA keys...")
        key = RSA.generate(keySize)
        print(keySize, "RSA keys generated.")
        print("Private key exporting...")
        private_key = key.export_key()
        file_out = open(priKeyFile, "wb")
        file_out.write(private_key)
        file_out.close()
        print("Private key exported.")
        print("Public key exporting...")
        public_key = key.publickey().export_key()
        file_out = open(pubKeyFile, "wb")
        file_out.write(public_key)
        file_out.close()
        print("Public key exported.")
        
        return True
        