
# peer_server.py
# to read the code start from the main fuction at the bottom and follow the comments

import sys, socket, select
import threading

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009
PEER_SERVERS = []

def peer_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:

        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
             
            # a message from a client, not a new connection
            else:
                
                try:
                    
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    
def broadcast (server_socket, sock, message):

    # sending message to clients
    
    for socket in SOCKET_LIST:
        # send the message only to clients
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

    #sending to other peers

    for socket in PEER_SERVERS:
        # send the message only to peers
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

def gateway_thread():
    gateway = sys.argv[1]
    port = int(sys.argv[2])
    try :
        s.connect((gateway, port))
    except :
        print 'Unable to connect to gateway'
        sys.exit()
     
    print 'Connected to gateway. Recieving Peer information'
    
     
    while 1:
       
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from gateway
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from gateway'
                    sys.exit()
                else :
                    #Peer list
                    PEER_SERVERS = data     
            


if __name__ == "__main__":

    
    # thread for gateway 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    ct = threading.Thread(target = gateway_thread, args = (s,))
    #gateway_thread method is invoked for this thread
    threadPool.append(ct)
    ct.start()
    # starting server
    sys.exit(peer_server())
    #peer_server(method is envoked)
