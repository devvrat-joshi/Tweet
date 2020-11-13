import socket
import sys
socket.setdefaulttimeout(3)
class client:
    def __init__(self,ip,port,command):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.sock.send(bytes(command,"utf-8"))
        data = ""
        try:
            while 1:
                k = self.sock.recv(10000).decode()
                data += k
                if not k:
                    break        
                # print(data)
        except socket.timeout:
            pass
while 1:
    command = input("Client : ")
    client("localhost",12345,command)