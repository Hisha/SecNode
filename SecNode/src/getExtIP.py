import urllib.request

class getExtIP():
    
    def __init__(self):
        self.ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')