
import socket
SIZE = 1024
FORMAT = "utf-8"

import ntpath

class Servidor:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    def __init__(self,port):
        ip = socket.gethostbyname(socket.gethostname())
        address = (ip, port)
        self.server.bind((address))
        self.server.listen()
    

    def hasClientCancelled(self, fileName):
        return fileName=='0'
  
    def acceptFileConfirmation(self, fileName):

        #print(f"Desea usted aceptar el archivo{fileName} escriba si o No")  (Vemos si llegamos con popup)
        return True
    
    def recieveFile(self,fileName,connection):
        connection.send(f"Comenzando transferencia de {fileName}".encode())
        data = connection.recv(SIZE).decode(FORMAT)
        with open(fileName, 'w') as file:    
                file.write(data)
                file.close


    def acceptMessageFlow(self,connection):
        fileName = connection.recv(SIZE).decode(FORMAT)
        if(self.hasClientCancelled(fileName)):
                print("El cliente no encotró el archivo y canceló la conexión")
                connection.send("Servidor: Hasta la proxima, esperamos que encuentre el archivo".encode())
        else:
            if(self.acceptFileConfirmation(fileName)):
                self.recieveFile(fileName,connection)
                connection.send(f"Servidor: Muchas gracias por la transferencia de {fileName}".encode())
                connection.close
            else:
                connection.send(f"Servidor: Decidimos rechazar el archivo {fileName}, disculpas".encode())
    


    def startConnection(self):
            while True:
                connection,address =self.server.accept()
                message = (f'Servidor: Se conectó al adress:{address}')
                connection.send(message.encode())
                self.acceptMessageFlow(connection)

            
        

def main():
    servidor = Servidor(8121)
    servidor.startConnection()
    


