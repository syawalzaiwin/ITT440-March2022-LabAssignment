import socket
import sys
import time
import errno
import math
from multiprocessing import Process



def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server\n'))
    while True:
        data = s_sock.recv(2048)
        print(data)
        if not data:
            break
        number = math.log2(data)
        s_sock.sendall(str.encode(number))
        
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.56.104',8000))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')
                
            except Exception as e:        
                print('an exception occurred!')
                print(e)
                sys.exit(1)
                
    finally:
     	   s.close()
