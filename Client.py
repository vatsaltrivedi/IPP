import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(1024)
print repr(data)
while True:
    msg = raw_input()
    s.sendall(msg)
    data=s.recv(2048)
    if not data:break
    print data
print "Server Stopped"

s.close()