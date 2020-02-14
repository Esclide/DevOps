import socket


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.start()

    def start(self):
        print('[-ip address] to show domain names by IP address\n'
              '[-add name:address] to add domain names and IP address\n[-q] to exit\n')
        while True:
            message = input('Enter message to send: \n')
            if message == "-q":
                break
            self.clientSocket.sendto(message.encode('utf-8'), self.address)
            self.clientSocket.settimeout(1)
            try:
                data = self.clientSocket.recvfrom(1024)
                reply = data[0]
                print(reply.decode('utf-8'))
            except Exception:
                print('The server is not available')
        self.clientSocket.close()


if __name__ == '__main__':
    client = Client('localhost', 7777)
