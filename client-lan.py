import socket

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

    def startConnection(self):
        self.cliente.connect(('192.168.56.1',PORT))
        self.cliente.send("prueba.txt".encode(FORMAT))
        print(self.getServerMessage())
        file = open("prueba.txt")
        data = file.read()
        self.cliente.send(data.encode(FORMAT))


def main():
   
    cliente = Client()
    cliente.startConnection()


main()