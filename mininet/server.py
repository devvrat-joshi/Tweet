import socket
import threading
from colorama import init, Fore, Back, Style

LOCK = threading.Lock()
socket.setdefaulttimeout(1)

from src.urls import functions
print(Fore.GREEN + 'Server started Listening' )
print(Style.RESET_ALL)

class server:
    def __init__(self,connections,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,True)
        self.sock.bind(("localhost",port))
        self.sock.listen(connections)
        self.threads = []

    def start(self):
        while 1:
            LOCK.acquire()
            self.threads.append(self.thread())

    @staticmethod
    def new_thread(c,address):
        try:
            while 1:
                data = c.recv(1024).decode().split()
                print(data)

        except socket.timeout:
            c.send(bytes(functions[data[0]](data[1:]),"utf-8"))
            LOCK.release()
            return
        LOCK.release()
  
    def thread(self):
        c,address = self.sock.accept()
        print(address)
        new = threading.Thread(server.new_thread(c,address))
        new.start()
        return new
while 1:
    try:
        S = server(1000,12345)

        S.start()
    except Exception:
        # print(Exception)
        try:
            LOCK.release()
        except:
            pass
        try:
            S.sock.close()
        except:
            pass
