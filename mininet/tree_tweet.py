# mininet modules
import time
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
# mininet instance
net = Mininet()
# add hosts
h1 = net.addHost('h1')  # h1 will be server
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
h6 = net.addHost('h6')
h7 = net.addHost('h7')
h8 = net.addHost('h8')
h9 = net.addHost('h9')
# add switches
d0s1 = net.addSwitch("d0s1")
d1s1 = net.addSwitch("d1s1")
d1s2 = net.addSwitch("d1s2")
d2s1 = net.addSwitch("d2s1")
d2s2 = net.addSwitch("d2s2")
d2s3 = net.addSwitch("d2s3")
d2s4 = net.addSwitch("d2s4")

# add controllers
c0=net.addController('c0')

# depth 0
net.addLink("h1","d0s1")
# depth 1
net.addLink("d1s1","d2s1")
net.addLink("d1s1","d2s2")
net.addLink("d1s2","d2s3")
net.addLink("d1s2","d2s4")
net.addLink("d0s1","d1s2")
net.addLink("d0s1","d1s1")
# depth 2
net.addLink("d2s1","h2")
net.addLink("d2s1","h3")
net.addLink("d2s2","h4")
net.addLink("d2s2","h5")
net.addLink("d2s3","h6")
net.addLink("d2s3","h7")
net.addLink("d2s4","h8")
net.addLink("d2s4","h9")
# start mininet emulator
net.start()
for controller in net.controllers:
    controller.start()
h1.cmd("python3 server_mn.py {} &".format(h1.IP())) # start server
print("server")
time.sleep(2)
h2.cmd("python3 chat_client_mn.py {} {} {} &".format(h2.IP(),h1.IP(),2))
h3.cmd("python3 chat_client_mn.py {} {} {} &".format(h3.IP(),h1.IP(),3))
h4.cmd("python3 chat_client_mn.py {} {} {} &".format(h4.IP(),h1.IP(),4))
h5.cmd("python3 chat_client_mn.py {} {} {} &".format(h5.IP(),h1.IP(),5))
h6.cmd("python3 chat_client_mn.py {} {} {} &".format(h6.IP(),h1.IP(),6))
h7.cmd("python3 chat_client_mn.py {} {} {} &".format(h7.IP(),h1.IP(),7))
h8.cmd("python3 chat_client_mn.py {} {} {} &".format(h8.IP(),h1.IP(),8))
h9.cmd("python3 chat_client_mn.py {} {} {} &".format(h9.IP(),h1.IP(),9))
files = []
hosts = [h2,h3,h4,h5,h6,h7,h8,h9]
CLI(net)
server_out = open("tests/output/server.txt","w")
for i in range(2,10):
    files.append(open("tests/output/client{}.txt".format(i),"w"))
try:
    numIter = 0
    while 1:
        numIter += 1
        time.sleep(1)
        server_out.write(h1.cmd(">"))
        for i in range(8):
            files[i].write(hosts[i].cmd(">"))
        if numIter % 3 == 0:
            server_out.flush()
            files[i].flush()
        # print(10)
except KeyboardInterrupt:
    for i in files:
        i.close()

# stop mininet emulator and exit
net.stop()
exit()