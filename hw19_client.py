import socket

host = 'localhost'
port = 7777
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input('Enter message to send \n[-ip address] to show domain names by IP address\n'
            '[-add name:address] to add domain names and IP address\n ')
client.sendto(msg.encode('utf-8'), (host, port))
d = client.recvfrom(1024)
reply = d[0]
addr = d[1]
print(reply.decode('utf-8'))
client.close()
