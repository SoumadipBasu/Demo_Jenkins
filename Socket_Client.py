import socket

client = socket.socket()
client.connect(('localhost',9996))

name = input('Enter Your Name')
client.send(bytes(name,'utf-8'))
print(client.recv(1024).decode())
