import socket
from os.path import exists

PORT =8121
ADDR = ("172.22.96.1", PORT)
FORMAT ="utf-8"
SIZE = 1024


class Client:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # dice que vamos a usar TCP, no se preocupa si recibe o mando
    cFilePath=""

    def __init__(self, port,ip,filePath):
        adress = (ip,int(port))
        self.cliente.connect(adress)
        print(self.getServerMessage())
        self.cFilePath=filePath

    def getServerMessage(self):
        message=self.cliente.recv(SIZE).decode(FORMAT)
        return message


    def sendFileName(self):
        print(self.cFilePath)
        self.cliente.send(self.cFilePath.encode(FORMAT))
    
    def sendFileData(self):
        print(self.cFilePath)
        file = open(self.cFilePath)
        data = file.read()
        print(data)
        self.cliente.send(data.encode(FORMAT))
        
        

    def sendFileFlow(self):
        print("Sending file data")
        self.sendFileName()
        print(self.getServerMessage())
        self.sendFileData()
        print(self.getServerMessage())
        print("termino")
     
    
            


