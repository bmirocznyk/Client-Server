
import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT =8121
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

class Servidor:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # dice que vamos a usar TCP, no se preocupa si recibe o mando
    server.bind((ADDR))# ip empty para que escuche otras requests de otras compus
    server.listen()

    def __init__(self):
       
        print("Listening")

    def hasClientCancelled(self, fileName):
        return fileName=='0'
  
    def acceptFileConfirmation(self, fileName):
        print(f"Desea usted aceptar el archivo{fileName} escriba Si o No")
        return input().upper =="SI"

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
                connection.send("Hasta la proxima, esperamos que encuentre el archivo".encode())
        else:
            if(self.acceptFileConfirmation):
                self.recieveFile(fileName,connection)
                connection.send(f"Muchas gracias por la transferencia de{fileName}".encode())
            else:
                connection.send(f"Decidimos rechazar el archivo{fileName}, disculpas".encode())
    


    def startConnection(self):
        while True:
            connection,address =self.server.accept()
            message = (f'Se conectó el adress:{address}')
            connection.send(message.encode())
            self.acceptMessageFlow(connection)
           

            
        

def main():
    servidor = Servidor()
    servidor.startConnection()
    


main()