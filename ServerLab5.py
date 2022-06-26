import socket
import sys
import json



s = socket.socket()
print("Socket successfully created")

port = 8080

s.bind(('', port))
print("socket binded to " + str(port))

s.listen(5)
print("socket is listening")

data = s.rcev(1024)
data = data.decode("utf-8")

dataJ = json.loads(data)

print (type(dataJ))
print(dataJ)

s.close()

