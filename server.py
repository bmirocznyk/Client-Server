
from sqlite3 import connect
import threading
from pstats import SortKey
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

    def startConnection(self):
        while True:
            connection,address =self.server.accept()
            message = (f'Te conectaste al mejor servidor{address}')
            connection.send(message.encode())
            filename = connection.recv(SIZE).decode(FORMAT)
            print(f"Starting to recieve{filename}")
            connection.send("Comenzando transferencia de {filename}".encode())
            data = connection.recv(SIZE).decode(FORMAT)
            print(f"Se recibio")
            
            print(data)

            with open('readme2.txt', 'w') as file:    
                file.write(data)
                file.close

        

def main():
    servidor = Servidor()
    servidor.startConnection()
    


main()