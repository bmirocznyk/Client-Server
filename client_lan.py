import socket
from os.path import exists
PORT =8121
ADDR = ("172.22.96.1", PORT)
FORMAT ="utf-8"
SIZE = 1024


class Client:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # dice que vamos a usar TCP, no se preocupa si recibe o mando

  

    def __init__(self, port,ip):
        adress = (ip,port)
        self.cliente.connect(adress)
        print(self.getServerMessage())
        self.sendFileFlow()

    def getServerMessage(self):
        message=self.cliente.recv(SIZE).decode(FORMAT)
        return message

    def selectFile(self):
        print("Ingrese nombre")
        fileName = input()
        fileExists= exists(fileName)
        
        while(not fileExists and fileName != "0"):
            

            print("No se encontró el archivo, intente nuevamente o ingrese 0 para finalizar")
            fileName= input()
            fileExists= exists(fileName)
       
        return fileName


    def checkIfFileExists(self,fileName):
        return fileName != "0"




    def sendFileName(self, fileName):
        self.cliente.send(fileName.encode(FORMAT))
    
    def sendFileData(self,fileName):
        file = open(fileName)
        data = file.read()
        self.cliente.send(data.encode(FORMAT))
        

    def sendFileFlow(self,path):
        fileName = self.selectFile()
        self.sendFileName(fileName)
        print(self.getServerMessage())
        if(self.checkIfFileExists(fileName)):
            self.sendFileData(fileName)
            print(self.getServerMessage())
            self.startMenu()
        else:
            print("Se canceló la busqueda")
            


