import socket
import threading

# amount of bytes that can be sent by clientn to server
HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECTED = "!DISCONNECTED"
# getting ip addr
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = "192.168.137.2"
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
                elif msg == "medical":
                    ip_to_be_sent = "127.0.1.1 8081"
                elif msg == "police":
                    ip_to_be_sent = "127.0.1.1 8081"
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