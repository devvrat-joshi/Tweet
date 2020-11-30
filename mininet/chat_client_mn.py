import socket
import sys, os
import atexit
import multiprocessing

# 1 : IP own, 2 : IP server, 3 : Client_id

manager = multiprocessing.Manager()
shared = manager.dict()
def server_chat(ip, port, shared):
    print("I am running")
    while 1:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,True)
            sock.bind((ip,port))
            sock.listen(5)
            c,addr = sock.accept()
            print("I accepted", addr)
            while 1:
                data = c.recv(1024).decode()
                print(data)
                if data=="":
                    break
        except socket.timeout:
            try:
                sock.close()
            except:
                pass



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


sessionID = client(sys.argv[2],12345,"init").data
sessionUser = 'guest'
print(sessionID)
def logout_exit():
    client(sys.argv[2], 12345, "logout")
server_process = multiprocessing.Process(target=server_chat,args=(sys.argv[1],int(sessionID)+1024,shared))
server_process.start()
atexit.register(logout_exit)
file = open("./tests/input/client{}.txt".format(sys.argv[3]),"r")
while 1:
    command = file.readline()
    if not command:
        break
    print("COMMAND :: " + command)
    if command.find("tweet")!=-1:
        s = file.readline()
        recData = client(sys.argv[2],12345,"tweet " + s + " " + sessionID).data
        print(recData)
        continue
    recData = client(sys.argv[2],12345,command+" "+sessionID).data
    if recData.find("$Logged_out$")!=-1 :
        sessionUser = "guest"
        print("Logged Out Successfully !!!")
        continue
    elif recData.find("Logged in ")!=-1 or recData.find("Welcome") != -1:
        sessionUser = command.split()[1]
    print(recData+"\n")