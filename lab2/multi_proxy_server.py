#!/usr/bin/env python3

# Code modififed from lab instruction

import socket, time, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):

    # Get the host IP from hostname
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    # Return the remote IP and host
    print(f"IP address of {host} is {remote_ip}")
    return remote_ip

def handle_request(conn, addr, proxy_end):
    
    # Receive data from the connection
    send_full_data = conn.recv(BUFFER_SIZE)
    print(f"Sending received data {send_full_data} to google")
    
    # Send all of the data received to the proxy_end connection
    proxy_end.sendall(send_full_data)
    # Shutdown further sends from the connection
    proxy_end.shutdown(socket.SHUT_WR)
    # Receive data sent to the connection
    data = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending received data {data} to client")
    # Send socket data to the server
    conn.send(data)

def main():

    host = "www.google.com"
    port = 80

    # Create socket, bind and set to listening mode
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            # Establish proxy_start, proxy_end and connect
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))
                # Run handle request with a proxy_start connection (local server) and address with a new proxy_end socket (Google)
                p = Process(target=handle_request, args=(conn, addr, proxy_end))
                p.daemon = True
                p.start()
                print("Started process ", p)
            conn.close()

if __name__ == "__main__":
    main()