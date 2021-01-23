# CMPUT 404 Lab 2

## Question 1

> How do you specify a TCP socket in Python?

Using the `socket` library, with the method `socket` the TCP socket is created for the `AF_INET` which provided the terminals hostname or IPv4 address, and the `SOCK_STREAM` specifies the socket type.

## Question 2

> What is the difference between a client socket and a server socket in Python?

A server socket will listen and accept connections from a client, then send and receive data with the client until the connection is closed.

Where as a client initiates a connection and sends/receives data with the server.
 
## Question 3

> How do we instruct the OS to let us reuse the same bidn port?

In the echo server, when setting the `setsocketopt()` provide the argument "socket.SO_REUSEADDR" which will instruct the local socket to be reused.

## Question 4

> What information do we get about incoming connections?

We get the address bound to the socket at the other end of the connection, consisting of a host and port.

## Question 5


> What is returned by `recv()` from the server after it is done sending the HTTP request?

The server prints out whatever message is sent to the server in the form of utf-8 bytes. This can be converted to a string in python to clean up the output, however in the example "Foobar" the output of the server is shown as `b'Foobar\n'`.

# Question 6

https://github.com/fredford/cmput404/tree/main/lab2

# Collaboration

Code was modified from what was provided and shown by the TA's in the lab.
