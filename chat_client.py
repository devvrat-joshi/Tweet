import socket       # socket
import sys, os      
import atexit       # runs at exit, keyboard interrupt.
import multiprocessing  
from getpass import getpass
from colorama import init, Fore, Back, Style

manager = multiprocessing.Manager()
shared = manager.dict()

#it runs a chat-server as a separate forked process in the background, which listens for receiving chat messages at client
def server_chat(ip, port, shared):
    while 1:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,True)
            sock.bind(("localhost",port))
            sock.listen(5)
            c,addr = sock.accept()
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


# Client side timeout
socket.setdefaulttimeout(3)

# make a TCP client.
class client:
    def __init__(self,ip,port,command):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP client
        self.sock.connect((ip,port))    # connect to the server
        self.sock.send(bytes(command,"utf-8"))
        data = ""
        try:
            while 1:
                k = self.sock.recv(10000).decode() # receive data
                data += k
                if not k:
                    break        
                
        except socket.timeout: # If timeout
            pass
        self.data = data  # return the results from the server

#if the client faces an exception or closes, makes sure that the user is logged out
def logout_exit():
    client("localhost", 12345, "logout")

#first generate a unique sessionID for the given client with the server
#every request after it contains the sessionID for the server to uniquely identify the client and the state of it
sessionID = client("localhost",12345,"init").data
#default is guest for client, when not logged in [ It is just for interface purpose]
sessionUser = 'guest'
print(sessionID)

server_process = multiprocessing.Process(target=server_chat,args=("localhost",int(sessionID)+1024,shared))
server_process.start()
atexit.register(logout_exit)

while True:
    command = input(Fore.YELLOW + "{} : ".format(sessionUser) + Fore.WHITE)
    #open the text editor, in case for tweet command to post a new tweet
    if command == "tweet":
        file = open("data/tweet{}.txt".format(sessionID),"w")
        file.close()
        os.system("nano data/tweet{}.txt".format(sessionID))
        command = input(Fore.YELLOW +  "Are you sure to post the tweet Y/N : " + Fore.WHITE)
        if command[0] == 'y' or command[0] == 'Y':
            tweet = open("data/tweet{}.txt".format(sessionID),"r")
            s = tweet.read(200)
            tweet.close()
            recData = client("localhost",12345,"tweet " + s + " " + sessionID).data
            print(recData)
        else :
            print(Fore.RED + "Post cancelled !" + Fore.WHITE)
        continue
    #take password as obscure input in case of login
    elif command[:5] == "login":
        password = getpass(Fore.BLUE + 'Password: ' + Fore.WHITE)
        command += " " + password
    #take password as obscure input two times in case of register
    elif command[:8] == "register":
        password = getpass(Fore.BLUE + 'Password: ' + Fore.WHITE)
        repassword = getpass(Fore.BLUE + 'Re-enter Password: ' + Fore.WHITE)
        command+=" "+password+" "+repassword
        
    #sessionID is sent with every request
    recData = client("localhost",12345,command+" "+sessionID).data

    #change the sessionUser variable (which just stores username for interface purpose) in case of logout or login or register
    if recData.find("$Logged_out$")!=-1 :
        sessionUser = "guest"
        print(Fore.GREEN + "Logged Out Successfully !!!" + Fore.WHITE)
        continue
    elif recData.find("Logged in ")!=-1 or recData.find("Welcome") != -1:
        sessionUser = command.split()[1]
    print(recData)
