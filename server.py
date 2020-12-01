import socket
import threading
from colorama import init, Fore, Back, Style

# Multi-threaded server
LOCK = threading.Lock()

from src.urls import functions
print(Fore.GREEN + 'Server started Listening' + Fore.WHITE)

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
        LOCK.release()
        try:
            data = c.recv(4096).decode().split()
            print(data)
            c.send(bytes(functions[data[0]](data[1:]),"utf-8"))
        except:
            pass
        return

    def thread(self):
        c,address = self.sock.accept()
        print(address)
        new = threading.Thread(server.new_thread(c,address))
        new.start()
        return new

S = server(1000,12345)
S.start()
