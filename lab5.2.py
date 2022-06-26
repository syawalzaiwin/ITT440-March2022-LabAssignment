import socket

s = socket.socket()

port = 8888

s.connect(('192.168.56.104', port))

data = s.recv(1024)

s.send('Hi, saya client. Terima Kasih!');

print (data)

s.close()

