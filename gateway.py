# gateway.py
 
import sys
import socket
import select

HOST = '' 
SOCKET_LIST = []
BUFFER = 4096 
PORT = 10001

def gateway():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)
    print "Gateway started on port " + str(PORT)

    while 1:
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
        for sock in ready_to_read:
           
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Peer (%s, %s) connected" % addr
                 
                send_list()
             
            
    server_socket.close()
    
def send_list(server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)




if __name__ == "__main__":

    sys.exit(gateway()) 
