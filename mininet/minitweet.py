import time
# Mininet Modules
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from os import fsync
#mininet instance
net = Mininet()
#adding components

output_files = []

hosts = []
numClients = 11

s1 = net.addSwitch('s1')
c0 = net.addController('s4')

server_out = open("./tests/output/server.txt","w")
h0 = net.addHost('h0')
net.addLink( h0, s1 )
for i in range(numClients):
    time.sleep(0.2)
    output_files.append(open("./tests/output/client{}.txt".format(i + 1),"w"))
    hosts.append(net.addHost('h{}'.format(i + 1)))
    net.addLink( hosts[i], s1 )

net.start() # mininet emulator started

print(h0.cmd("python3 server_mn.py {} &".format(h0.IP()))) # h0 host is server
time.sleep(2)
for i in range(numClients):
    hosts[i].cmd("python3 chat_client_mn.py {} {} {} &".format(hosts[i].IP(),h0.IP(),i + 1)) # client

# CLI(net)
try:
    numIter = 0
    while 1:
        numIter += 1
        time.sleep(1)
        server_out.write(h0.cmd(">"))
        for i in range(numClients):
            output_files[i].write(hosts[i].cmd(">"))
        if numIter % 3 == 0:
            server_out.flush()
            output_files[i].flush()
        # print(10)
except KeyboardInterrupt:
    for i in output_files:
        i.close()


# print(h0.cmd(">"))
# h3.cmd("python3 Q3client.py 2 'client 2 asking for book 2' &") # client
# h4.cmd("python3 Q3client.py 3 'client 3 asking for book 3' &") # client
# h5.cmd("python3 Q3client.py 4 'client 4 asking for book 4' &") # client
# h6.cmd("python3 Q3client.py 5 'client 5 asking for book 5' &") # client
# time.sleep(3)
# print("client : h3 --- Output ----\n"+h3.cmd(">")) # client output
# print("client : h4 --- Output ----\n"+h4.cmd(">")) # client output
# print("client : h5 --- Output ----\n"+h5.cmd(">")) # client output
# print("client : h6 --- Output ----\n"+h6.cmd(">")) # client output
# #stop mininet emulator and exit
# CLI(net)
net.stop()
exit()