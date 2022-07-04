# Socket-Programing-using-python
A simple Programing simulating Emergency services Complaint Registration using TCP sockets.
## What is this ?

  This python program utilzes AF_INET streaming sockets in other words,it sets up a TCP  IPv4 only connections
  so ensure that the client,server and the service_server processes are all connected within the same netwrok/router.

  Also,this code should be able to run in any OS/machine with a built-in python 3.x Interperter it should be noted that 
  it was tested extensively on a GNU/Linux machine having Python 3.8.10 interperter and a Windows 10 Computer.

##How does this work?

  magic.
##How To Run This?

 * Run server.py
    ```python3 server.py'''
 * Run service.py
    ```python3 service_server.py'''
 * Finally run client.py
    ```python3 client.py'''
 
##
Anbox is currently suited for the desktop use case but can be used on mobile
operating systems like [Ubuntu Touch](https://ubuntu-touch.io/) or
[postmarketOS](https://postmarketos.org)
([installation instructions](https://wiki.postmarketos.org/wiki/Anbox)).
However this is still a work in progress.

The Android runtime environment ships with a minimal customized Android system
image based on the [Android Open Source Project](https://source.android.com/).
The used image is currently based on Android 7.1.1
```sh
adb install xyz.apk
```
