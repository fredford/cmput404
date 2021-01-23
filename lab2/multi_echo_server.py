#!/usr/bin/env python3

# Code modified from lab presentation

import socket
import time
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():

    # Create an IPv4 socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # Set the ability for address reuse
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind socket to address
        s.bind((HOST, PORT))
        # Set to listening mode
        s.listen(2)
        # Continuously listen for connections
        while True:
            # Accept socket connection
            conn, addr = s.accept()
            # Process handling the echo for the address and connection provided
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

def handle_echo(addr, conn):
    print("Connected by ", addr)

    # Receive data and send it back before shutting down
    full_data = conn.recv(BUFFER_SIZE)
    # Send all data and close the connection
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()