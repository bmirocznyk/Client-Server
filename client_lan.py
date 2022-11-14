import socket
from os.path import exists, basename

FORMAT ="utf-8"
SIZE = 1024


class Client:
    
    cliente =""
    cFilePath=""

    
    def __init__(self, port,ip,filePath):
        self.cliente=cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        adress = (ip,int(port))
        self.cliente.connect(adress)
        print(self.getServerMessage())
        self.cFilePath=filePath
    


    def getServerMessage(self):
        message=self.cliente.recv(SIZE).decode(FORMAT)
        return message


    def sendFileName(self):
        fileName = basename(self.cFilePath)
        self.cliente.send(fileName.encode(FORMAT))
    
    def sendFileData(self):
        file = open(self.cFilePath)
        data = file.read()
        self.cliente.send(data.encode(FORMAT))
    
        
        

    def sendFileFlow(self):
        print("Sending file data")
        self.sendFileName()
        print(self.getServerMessage())
        self.sendFileData()
        print(self.getServerMessage())
        print("termino")
        self.cliente.close()
        
     
    
            


