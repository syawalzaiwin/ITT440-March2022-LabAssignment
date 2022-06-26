import socket
import sys
import json

s = socket.socket()

port = 8080

s.connect(('192.168.56.104', port))

name = input("Enter your name: ")
age = input("You Age: ")

sendData = json.dumps(name, age)

while True:
        c, addr = s.accept()
        print("Got connection from" + str(addr))

        c.sendall(bytes(sendData,encoding="utf-8"))
        buffer = c.recv(1024)
        print(buffer)
c.close()
