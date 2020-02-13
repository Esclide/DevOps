
import socket
import sys
import threading

class Client:

    isStarted = False
    SIZE = 1024
    ENC = "UTF-8"

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = socket.socket()
        try:
            self.clientSocket.connect((host, port))
            self.isStarted = True
            self.getNickname()
            self.receiveThread = threading.Thread(target=self.receiveMessage)
            self.sendThread = threading.Thread(target=self.sendMessage)
            self.receiveThread.start()
            self.sendThread.start()
        except Exception:
            print("The server is unavailable")

    def sendMessage(self):
        while self.isStarted:
            message = input()
            self.clientSocket.send(bytes(message, self.ENC))
            if message == '-quit':
                self.exitChat()

    def receiveMessage(self):
        while self.isStarted:
            data = self.clientSocket.recv(self.SIZE)
            if not data:
                break
            print(data.decode(self.ENC))

    def exitChat(self):
        self.clientSocket.close()
        print("Your connection was closed")
        self.isStarted = False
        quit()
        exit(-1)
        sys.exit()

    def getNickname(self):
        data = self.clientSocket.recv(self.SIZE).decode(self.ENC)
        print(data)
        message = input()
        self.clientSocket.send(bytes(message, self.ENC))




if __name__ == '__main__':

    client = Client('127.0.0.1', 9103)

