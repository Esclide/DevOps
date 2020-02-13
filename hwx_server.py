import socket
from _thread import start_new_thread
from threading import Thread


class Server:
    clientsDict = {}
    nicknamesDict = {}
    SIZE = 1024
    ENC = "UTF-8"

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((host, port))
        print('Server is running, please, press ctrl+c to stop')
        print('Waiting for connections...')

    def startServer(self, maxConnections):
        try:
            self.serverSocket.listen(maxConnections)
            while True:
                connection, address = self.serverSocket.accept()
                print("{}:{} was connected.".format(address, address))
                self.getNickname(connection)
                self.clientsDict[connection] = address
                start_new_thread(self.acceptConnections, (connection,))
            connection.close()
        except KeyboardInterrupt:
            print("\nThe server was stopped")

    def getNickname(self, connection):
        connection.send(bytes('Please enter your nickname', self.ENC))
        nickname = connection.recv(self.SIZE).decode(self.ENC)
        self.nicknamesDict[connection] = nickname
        message = 'Welcome to server, ' + str(nickname) + '!\nType -help to see chat commands'
        self.broadcast('[SYSTEM]', bytes('{} was connected to chat'.format(nickname), self.ENC))
        connection.send(bytes(message, self.ENC))

    def sendHelp(self, connection):
        help_message = '-chname - change nickname\n' \
                       '-userlist - show list of users in room ' \
                       '-quit - exit from the chat'
        connection.send(bytes(help_message, self.ENC))

    def acceptConnections(self, connection):
        while True:
            message = connection.recv(self.SIZE)
            if not message:
                break
            if message == bytes("-quit", self.ENC):
                address = self.clientsDict[connection]
                print("{}:{} was disconnected.".format(address, address))
                self.broadcast('[SYSTEM]', bytes('{} was disconnected from chat'.format(self.nicknamesDict[connection]), self.ENC))
                self.delConnection(connection)
            if message == bytes("-help", self.ENC):
                self.sendHelp(connection)
            if message == bytes("-chname", self.ENC):
                self.changeNickname(connection)
            if message == bytes("-userlist", self.ENC):
                self.sendUserlist(connection)
            else:
                try:
                    self.broadcast(self.nicknamesDict[connection], message)
                except Exception:
                    pass

    def broadcast(self, nickname, message):
        for clientSocket in self.clientsDict.keys():
            clientSocket.send(bytes('{}:{}'.format(nickname, message.decode(self.ENC)), self.ENC))

    def sendUserlist(self, connection):
        connection.send(bytes('{0:>10}     {1:10}'.format("address", "nickname"), self.ENC))
        for client in self.nicknamesDict:
            connection.send(
                bytes("{0:10} ==> {1:10}\n".format(self.clientsDict[client][1], self.nicknamesDict[client]), self.ENC))

    def changeNickname(self, connection):
        connection.send(bytes('Please enter your nickname', self.ENC))
        nickname = connection.recv(self.SIZE).decode(self.ENC)
        self.nicknamesDict[connection] = nickname
        connection.send(bytes('Your nickname now is {} \n'.format(nickname), self.ENC))

    def delConnection(self, connection):
        self.clientsDict.pop(connection)

        self.nicknamesDict.pop(connection)


if __name__ == '__main__':
    server = Server('127.0.0.1', 9103)
    server.startServer(10)
