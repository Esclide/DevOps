import socket


class ServerDNS:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_address = (host, port)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def serverStart(self):
        self.serverSocket.bind(self.server_address)

        while True:
            print('Waiting for requests...')
            data = self.serverSocket.recvfrom(1024)
            received_msg = data[0]
            address = data[1]
            print('{}: {}'.format(address, received_msg))

            if data[0].decode('utf-8').split(" ")[0] == '-add':
                dnsList = self.getNameByIp(received_msg.decode("utf-8").split(" ")[1])
                self.sendDnsAnswer(dnsList, address)
            if data[0].decode('utf-8').split(" ")[0] == '-ip':
                dnsList = self.getNameByIp(received_msg.decode("utf-8").split(" ")[1])
                self.sendDnsAnswer(dnsList, address)
            else:
                dnsList = self.getIPByName(received_msg.decode("utf-8"))
                self.sendDnsAnswer(dnsList, address)

        self.serverSocket.close()

    def sendDnsAnswer(self, dnsList, address):
        if len(dnsList) > 0:
            self.sendIpList(dnsList, address)
        else:
            message = "{0:10} {1:10}\nNo required data on server".format("Server:", self.host)
            self.serverSocket.sendto(message.encode('utf-8'), address)


    def getIPByName(self, name):
        ipList = []
        with open("dns_addresses") as file:
            for line in file.readlines():
                if line.split(" ==> ")[0] == name:
                    ipList.append(line)
        return ipList

    def getNameByIp(self, ip):
        ipList = []
        with open("dns_addresses") as file:
            for line in file.readlines():
                if line.split(" ==> ")[1].strip() == ip.strip():
                    ipList.append(line)
        return ipList

    def sendIpList(self, ipList, address):
        message = "{0:10} {1:10}\n\n".format("Server:", self.host)
        for ipAddr in ipList:
            message += "{0:10}  {1:10}\n".format("Name:", ipAddr.split(" ==> ")[0]) + \
                       "{0:10}  {1:10}".format("Address:", ipAddr.split(" ==> ")[1])
        self.serverSocket.sendto(message.encode("UTF-8"), address)


if __name__ == '__main__':
    server = ServerDNS('localhost', 7777)
    server.serverStart()
