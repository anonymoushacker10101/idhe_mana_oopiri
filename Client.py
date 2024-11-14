import socket

c = socket.socket()  # you can mention the two arguments, if u want to change the default arguments
# connecting to the server
# Pass two pararmeters - IP address of the server and port no. which u want to connect with
c.connect(('localhost',19))  # ip address of the server
# asking the user to send the nameR
name = input('Enter your name:')
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())  # set buffer size