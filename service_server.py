import socket
import threading
import os
# amount of bytes that can be sent by clientn to server
HEADER = 64
PORT = 8081#this can be changed the port 8081 is already under use by another process
FORMAT = 'utf-8'
DISCONNECTED = "!DISCONNECTED"
DIR = "COMPLAINTS"#The service_server programs uses a directory called COMPLAINTS wheere it stores each individuals complaints
#To be changed
SERVER = socket.gethostbyname(socket.gethostname())#returns local host I.P but can be changed refer to server.py for more details
#SERVER = "192.168.137.2"
# creating a socket that looks for IPV4 address and takes TCP service from transport layer.
ADDR  = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(connectionSocket, addr):
    print(f"[New connection] {addr} connected")

    connected = True
    ip_to_be_sent = ""
    while connected:
           resp = "Complaint recieved..."
           connectionSocket.send("Post Your complaint".encode(FORMAT))
           resp = connectionSocket.recv(3000).decode(FORMAT)
           if resp == "NO":
               connected = False
               resp = DISCONNECTED
           elif resp == DISCONNECTED:
               connected = False
           else:
               data = resp.split("\n") #name@addr@complaint -->[name,addr,complaint]
               length=len(data);
               name = data[0]
               addr_field = data[1]
               compliant_field=data[2];
               filepath = os.path.join(DIR, name + ".txt")
               #receiving the data and storing it in a file 
               with open(filepath, "a+") as f:
                   f.write(f"name : {name}\nAddress:{addr_field}\nComplaint:{compliant_field}"+"\n")
           connectionSocket.send('Your complaint has been Registered'.encode(FORMAT))
           
    connectionSocket.close()


def start():
    server.listen()
    print(f"[LSITENING] SERVER IS LISTENING ON {SERVER}")
    while True:
        connectionSocket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (connectionSocket, addr))
        thread.start()#creating a thread 
        print(f"[Active connections] {threading.active_count()-1}")
start()
