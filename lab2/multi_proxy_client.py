#!/usr/bin/env python3

# Code modified from lab instruction

import socket
from multiprocessing import Pool

HOST = "localhost"
PORT = "8001"
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        # Create socket, connect, send & receive, then shutdown
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(f"Sending received data {full_data} to google")
        
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():

    address = [('127.0.0.1', 8001)]

    # Establish 10 different connections
    with Pool() as p:
        p.map(connect, address * 10)

if __name__ == "__main__":
    main()