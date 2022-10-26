

import socket
import sys
from unicodedata import name

IP = socket.gethostbyname(socket.gethostname())
PORT =8121
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

class Servidor:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # dice que vamos a usar TCP, no se preocupa si recibe o mando
    server.bind((ADDR))# ip empty para que escuche otras requests de otras compus
    server.listen()
    print(IP)
    def __init__(self):
       
        print("Listening")

    def startConnection(self):
        while True:
            clientsocket,address =self.server.accept()
            message = (f'Te conectaste al mejor servidor{address}')
            clientsocket.send(message.encode())
            filename = clientsocket.recv(SIZE).decode(FORMAT)
            print(f"Comienza la transferencia de :{filename}")
            clientsocket.send("Comenzando transferencia de {filename}".encode())
            data = clientsocket.recv(SIZE).decode(FORMAT)
            print(f"Se recibio")
            
            print(f"Datos de archivo:{data}")

            with open('readme.txt', 'w') as file:    
                file.write(data)
                file.close

          


    

def main():
    servidor = Servidor()
    servidor.startConnection()
    


main()