import socket,re


class ServerDNS:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_address = (host, port)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def serverStart(self):
        self.serverSocket.bind(self.server_address)
        try:
            while True:
                print('Server is running, please, press ctrl+c to stop')
                print('Waiting for requests...')
                while True:
                    data = self.serverSocket.recvfrom(1024)
                    self.handleData(data)
            self.serverSocket.close()
        except KeyboardInterrupt:
            print("\nThe server was stopped")

    def handleData(self, data):
        received_msg = data[0]
        address = data[1]
        print('{}: {}'.format(address, received_msg.decode('utf-8')))

        if data[0].decode('utf-8').split(" ")[0] == '-add':
            checksum = self.addRecord(received_msg.decode("utf-8").split(" ")[1])
            if checksum == 1:
                self.serverSocket.sendto("[SUCCESS] Address successfully added".encode('utf-8'), address)
                return
            elif checksum == -1:
                self.serverSocket.sendto("[ERROR] This IP address already in list".encode('utf-8'), address)
                return
            elif checksum == -2:
                self.serverSocket.sendto("[ERROR] Incorrect IP address".encode('utf-8'), address)
                return
            else:
                self.serverSocket.sendto("[ERROR] Error adding address".encode('utf-8'), address)
                return

        if data[0].decode('utf-8').split(" ")[0] == '-ip':
            dnsList = self.getNameByIp(received_msg.decode("utf-8").split(" ")[1])
            self.sendDnsAnswer(dnsList, address)
        else:
            dnsList = self.getIPByName(received_msg.decode("utf-8"))
            self.sendDnsAnswer(dnsList, address)

    def addRecord(self, message):
        tpl = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        if len(message.split(":"))<2: return 0
        name = message.split(":")[0]
        address = message.split(":")[1]
        if re.match(tpl, address) is None:
            return -2

        if self.ifIpInFile(address):
            return -1
        record = "{} ==> {}\n".format(name, address)
        try:
            with open("dns_addresses", 'a') as file:
                file.write(record)
                return 1
        except Exception:
            return 0

    def ifIpInFile(self, address):
        with open("dns_addresses") as file:
            for line in file.readlines():
                if (line.split(" ==> ")[1].strip() == address):
                    return 1
        return 0

    def sendDnsAnswer(self, dnsList, address):
        if len(dnsList) > 0:
            self.sendIpList(dnsList, address)
        else:
            message = "{0:10} {1:10}\nNo required data on server\n".format("Server:", self.host)
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
