import socket       # Socket
import threading    # Threading
from colorama import init, Fore, Back, Style

# Multi-threaded server
LOCK = threading.Lock()

from src.urls import functions
print(Fore.GREEN + 'Server started Listening' + Fore.WHITE)

class server:
    """
        Create a server.
    """
    def __init__(self,connections,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP server
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)   # reuse address
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,True)   # reuse port
        self.sock.bind(("localhost",port)) 
        self.sock.listen(connections)
        self.threads = []           # Thread ids stored

    def start(self):
        while 1:
            LOCK.acquire()      # If the main thread is not able to run, then acquire the lock.
            self.threads.append(self.thread())  # Start new thread

    @staticmethod
    def new_thread(c,address):
        LOCK.release()      # Whenever a new thread is started, let the main thread have the control.
        try:
            data = c.recv(4096).decode().split()        # Queries cannot be more than 4KB in size, by the design.
            print(data)
            c.send(bytes(functions[data[0]](data[1:]),"utf-8"))     # Run the corresponsing function of the query command and return the output of it.
        except:
            pass
        return

    def thread(self):
        c,address = self.sock.accept()      # Accept a connection and make a new thread and let that thread handle the query/request.
        print(address)
        new = threading.Thread(server.new_thread(c,address))    # start new thread
        new.start()
        return new

S = server(1000,12345)  # create a server
S.start()   # start the server
