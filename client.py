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
        self.data = data

    
sessionID = client("localhost",12345,"init").data
sessionUser = 'guest'
print(sessionID)
while 1:
    command = input("{} : ".format(sessionUser))
    recData = client("localhost",12345,command+" "+sessionID).data
    if recData.find("$Logged_out$")!=-1 :
        sessionUser = "guest"
        print("Logged Out Successfully !!!")
        continue
    elif recData.find("Logged in ")!=-1 or recData.find("Welcome") != -1:
        sessionUser = command.split()[1]
    print(recData)