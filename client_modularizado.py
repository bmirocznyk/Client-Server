import socket
from os.path import exists
IP = socket.gethostbyname(socket.gethostname())
PORT =8121
ADDR = (IP, PORT)
FORMAT ="utf-8"
SIZE = 1024


class Client:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # dice que vamos a usar TCP, no se preocupa si recibe o mando

  

    def __init__(self):
        print("Starting")
        

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


    def sendFileName(self, fileName):
        self.cliente.send(fileName.encode(FORMAT))
  
  

    def startConnection(self):
        self.cliente.connect(ADDR)
        print(self.getServerMessage())
        fileName = self.selectFile()
        self.sendFileName(fileName)
        print(self.cliente.recv(SIZE).decode(FORMAT))
        file = open("readme.txt")
        data = file.read()
        self.cliente.send(data.encode(FORMAT))
        print(self.cliente.recv(SIZE).decode(FORMAT))


def main():
   
    cliente = Client()
    cliente.startConnection()


main()