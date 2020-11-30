import socket
import threading
import sys

LOCK = threading.Lock()
from urls import functions

class server:
    def __init__(self, connections , ip , port ):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,True)
        self.sock.bind(( ip , port ))
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
            if data[0]=="login":
                c.send(bytes(functions[data[0]](data[1:]+[address[0]]),"utf-8"))
            else:
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

S = server(1000,sys.argv[1],12345)
S.start()
