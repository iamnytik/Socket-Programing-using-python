import socket

HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECTED = "!DISCONNECTED"
#SERVER = "192.168.137.2"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
#Here we are creating a TCP Socket connection
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)#This function sends and returns data from server.py
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(2048).decode(FORMAT)

def service(ip_addr, portToconnect):
    client_service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service_ADDR = (ip_addr, portToconnect)
    client_service.connect(service_ADDR)
    print(client_service.recv(2048).decode())# This fucntion formats our complaint and sends it to the
    print('Enter your name:-')#service
    resp = input()+"\n"#name@addr@comp 
    adder=input("now enter your address:-");
    resp=resp+adder+"\n"
    comp= input("Now enter your complaint:-");
    resp=resp+comp;
    resp = resp.encode(FORMAT)
    client_service.send(resp)
    print(client_service.recv(2048).decode(FORMAT))
    client_service.send(DISCONNECTED.encode(FORMAT))

print("1.Police Service\n2.Medical service\n")#Starts here
want = input()
response = send(want)#sending which service we want to the server and checking if sucessful
if response != DISCONNECTED :
    send(DISCONNECTED)#we close the connection with the server
elif response == DISCONNECTED:
    print("Service not available at server.")
client.close()
ip_addr = response.split(" ")[0]
portToConnect = int(response.split(" ")[1])#we receive  the IP and port number of the service_server
print(ip_addr)
print(portToConnect)
service(ip_addr, portToConnect)#now we connect to the service to register our complaint
