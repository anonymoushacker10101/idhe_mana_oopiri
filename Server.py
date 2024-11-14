import socket
s = socket.socket()
print('Socket is created')
s.bind(('localhost',19))
s.listen(1)
print('Waiting for connections')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with', addr, name)
    c.send(bytes('Welcome to socket connection','utf-8'))
    c.close()