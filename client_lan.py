import socket
from os.path import exists
IP = socket.gethostbyname(socket.gethostname())
PORT =8121
ADDR = ("172.22.96.1", PORT)
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


    def checkIfFileExists(self,fileName):
        return fileName != "0"




    def sendFileName(self, fileName):
        self.cliente.send(fileName.encode(FORMAT))
    
    def sendFileData(self,fileName):
        file = open(fileName)
        data = file.read()
        self.cliente.send(data.encode(FORMAT))
        

    def sendFileFlow(self):
        fileName = self.selectFile()
        self.sendFileName(fileName)
        print(self.getServerMessage())
        if(self.checkIfFileExists(fileName)):
            self.sendFileData(fileName)
            print(self.getServerMessage())
            self.startMenu()
        else:
            print("Se canceló la busqueda")
            
            

    def startConnection(self):
        self.cliente.connect(ADDR)
        print(self.getServerMessage())
        self.sendFileFlow()

        

    def startMenu(self):
        print("Seleccione 1 para enviar un archivo o 0 para cerrar la conexión")
        choice = input()
        if(choice=="1"):
            self.startConnection()
        elif (choice=="0"):
            print("Hasta la proxima")

def main():
   
    cliente = Client()
    cliente.startMenu()


main()