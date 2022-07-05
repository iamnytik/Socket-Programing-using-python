# Socket-Programing-using-python
A simple Programing simulating Emergency services Complaint Registration using TCP sockets.
A client contacts a server to get a service(police or medical)
and gets connected to the service server to register the complaint.
## What is this ?

  This python program utilzes AF_INET streaming sockets in other words,it sets up a TCP  IPv4 only connections
  so ensure that the client,server and the service_server processes are all connected within the same netwrok/router.

  Also,this code should be able to run in any OS/machine with a built-in python 3.x Interperter it should be noted that 
  it was tested extensively on a GNU/Linux machine having Python 3.8.10 interperter and a Windows 10 Machine.

## How does this work?
  ![info.png](https://user-images.githubusercontent.com/91942626/177193455-9dff60b9-d379-4493-bbcd-58e0a644c898.png)

   1.The Client process Establishes a connection with the server processs requesting a paticular Emergency service ("police"/"medical")
   
   2.The server then responds with the I.P and port number which the client uses to contact the requested service
   
   3.The client then connects with  the service_server and fills up the data form which is registered as new file in the COMPLAINTS folder
   
   4.The service_server then sends an acknowledgement back to the client and  all connections are closed
   
   
## How To Run This?
1)Run the server
 
    python3 server.py
    
2)Run the Service server

    python3 service_server.py
    
3)Finally run  the client

    python3 client.py


