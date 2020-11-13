import socket
import sys
socket.setdefaulttimeout(3)
class client:
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.sock.send(bytes("GET /page","utf-8"))
        data = ""
        try:
            while 1:
                k = self.sock.recv(10000).decode()
                data += k
                if not k:
                    file = open("index.html","w")
                    file.write(data)
                    file.close()
                    break        
                # print(data)
        except socket.timeout:
            file = open("index.html","w")
            file.write(data)
            file.close()
client("localhost",12345)
print(sys.argv)