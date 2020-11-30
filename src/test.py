import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost",1027))
sock.send(bytes("this is chat message","utf-8"))
sock.close()

"""
sachin1 --> sachin2
1. Search who all are online.
-->"chat sachin1"
-->"msg hi sachin, how are you?"
--> chat sachin2


(main server)->(sachin1 (server))  sachin2 is chatting 
sachin1 (client) -> (main server) give this "message" to sachin 1
(main server)->(sachin2 (server)) sachin1 is chatting 
sachin2 (client) -> (main server) give this "message" to sachin 2


"""