import socket
import threading

# amount of bytes that can be sent by clientn to server
HEADER = 64
PORT = 8080#this can be changed if port 8080 is already under use by another process
FORMAT = 'utf-8'
DISCONNECTED = "!DISCONNECTED"
# getting ip addr
SERVER = socket.gethostbyname(socket.gethostname())#this returns localhost IP but can be changed to something as shown below
#SERVER = "192.168.137.2" use ifconfig(or ipconfig) to select the right IP number and ensure that this IP(and the service IP below) lies in the same network

# creating a socket that looks for IPV4 address and takes TCP service from transport layer.
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(connectionSocket, addr):
    print(f"[New connection] {addr} connected")

    connected = True
    ip_to_be_sent = ""
    while connected:
            msg_length = connectionSocket.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg = connectionSocket.recv(HEADER).decode(FORMAT)
                if msg == DISCONNECTED:
                    connected = False
                    print(connectionSocket)
                elif msg == "medical":#medical service IP
                    ip_to_be_sent = "127.0.1.1 8081"#the IP and Port address can be changed 
                elif msg == "police":#police service IP
                    ip_to_be_sent = "127.0.1.1 8081"#the IP and Port address can be changed 
                else:
                    ip_to_be_sent = DISCONNECTED
                #print(f"{msg}")
                connectionSocket.send(ip_to_be_sent.encode(FORMAT))
    connectionSocket.close()


def start():
    server.listen()
    print(f"[LSITENING] SERVER IS LISTENING ON {SERVER}")
    while True:
        connectionSocket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (connectionSocket, addr))
        thread.start()
        print(f"[Active connections] {threading.active_count()-1}")
start()
