# gateway.py
# to read the code start from the main fuction at the bottom and follow the comments

import sys, socket,select

HOST = '' 
SOCKET_LIST = []
BUFFER = 4096 
PORT = 10001

def gateway():
    # start a socket on the machine listening on port 10001
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)
    print "Gateway started on port " + str(PORT)
    # whenever a new connection happens send the updated socket list to all the nodes
    while 1:
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
        for sock in ready_to_read:
           
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Peer (%s, %s) connected" % addr
                 
                send_list()
             
            
    server_socket.close()
    
def send_list():
    for socket in SOCKET_LIST:
        # send all the sockets only to peers
        try :
            socket.send(SOCKET_LIST)
        except :
            socket.close()
            if socket in SOCKET_LIST:
                SOCKET_LIST.remove(socket)




if __name__ == "__main__":
    # gateway method invoked 
    sys.exit(gateway()) 
