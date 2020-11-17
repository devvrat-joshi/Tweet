import socket
import sys, os

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
    if command == "tweet":
        file = open("data/tweet{}.txt".format(sessionID),"w")
        file.close()
        os.system("nano data/tweet{}.txt".format(sessionID))
        command = input("Are you sure to post the tweet Y/N : ")
        if command[0] == 'y' or command[0] == 'Y':
            tweet = open("data/tweet{}.txt".format(sessionID),"r")
            s = tweet.read(200)
            tweet.close()
            recData = client("",12345,"tweet " + s + " " + sessionID).data
            print(recData)
        else :
            print("Post cancelled !")
        continue
    recData = client("",12345,command+" "+sessionID).data
    if recData.find("$Logged_out$")!=-1 :
        sessionUser = "guest"
        print("Logged Out Successfully !!!")
        continue
    elif recData.find("Logged in ")!=-1 or recData.find("Welcome") != -1:
        sessionUser = command.split()[1]
    print(recData)