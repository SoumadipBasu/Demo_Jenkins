import socket

server = socket.socket()
print('Server Created')

server.bind(('localhost',9991))
server.listen(3)
print('Waiting for connections')

while True:
   client, address = server.accept()
   name = client.recv(1024).decode()
   print('Server Connected to: ',address,name)
   client.send(bytes('Welcome to Socket Server','utf-8'))

   client.close()