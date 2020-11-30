import time
# Mininet Modules
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

#mininet instance
net = Mininet()
#adding components
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
h6 = net.addHost('h6')
s1 = net.addSwitch('s1')
c0 = net.addController('s4')
net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.addLink( h3, s1 )
net.addLink( h4, s1 )
net.addLink( h5, s1 )
net.addLink( h6, s1 )
net.start() # mininet emulator started
h1.cmd("python3 server_mn.py {} &".format(h1.IP())) # h1 host is server
time.sleep(2)
h2.cmd("python3 chat_client_mn.py {} {} &".format(h2.IP(),h1.IP())) # client
time.sleep(2)
print(h1.cmd(">"))
# h3.cmd("python3 Q3client.py 2 'client 2 asking for book 2' &") # client
# h4.cmd("python3 Q3client.py 3 'client 3 asking for book 3' &") # client
# h5.cmd("python3 Q3client.py 4 'client 4 asking for book 4' &") # client
# h6.cmd("python3 Q3client.py 5 'client 5 asking for book 5' &") # client
time.sleep(3)
print("client : h2 --- Output ----\n"+h2.cmd(">")) # client output
# print("client : h3 --- Output ----\n"+h3.cmd(">")) # client output
# print("client : h4 --- Output ----\n"+h4.cmd(">")) # client output
# print("client : h5 --- Output ----\n"+h5.cmd(">")) # client output
# print("client : h6 --- Output ----\n"+h6.cmd(">")) # client output
# #stop mininet emulator and exit
CLI(net)
net.stop()
exit()