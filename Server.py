import socket
import threading

def threadedServer(conn):
    msg = "Connected to server"    
    conn.sendall(msg)
    
    while True:
        data = conn.recv(2048)
        
        x = list(repr(data))
        
        if not data: break
        if x[1:13] == ['K','I','L','L','_','S','E','R','V','I','C','E']:
            global kill
            global s
            kill = True
            print "Server closing down"
            
            conn.close()
            p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            p.connect(("localhost", 50007))
            p.close()
            
            s.close()             
            break
        elif x[1:5] == ['H','E','L','O']:
            msg = repr(data) + "\nIP: "+ addr[0] + "\nPort: " +str(addr[1])+ "\nStudent ID:14306119" 
            conn.sendall(msg)
        
        else: pass
if __name__ == '__main__':
    HOST = 'localhost'                 # Symbolic name meaning the local host
    PORT = 50007              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print "Waiting for clients..."
    threadPool = []
    kill = False
    while (not kill):
        conn, addr = s.accept()
        print 'Connected by', addr
        ct = threading.Thread(target = threadedServer, args = (conn,))
        threadPool.append(ct)
        ct.start()

    s.close()
    
    
        
    
    

      
    
