#!/usr/bin/env python3

import socket, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    # Try getting the IP of the host connection
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    # Return the IP and host of the connection
    print(f"IP address of {host} is {remote_ip}")
    return remote_ip

def main():

    host = 'www.google.com'
    port = 80
    # Create an IPv4 socket as proxy_start
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        # Set the socket for reuse
        proxy_start.set_socket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the provided host and port to the socket
        proxy_start.bind((HOST, PORT))
        # Listen for connections
        proxy_start.listen(1)
        while True:
            # Accept incoming connections
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            # Create an IPv4 socket to send the data back from the incoming connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))

                send_full_data = conn.recv(BUFFER_SIZE)

                print(f"Sending received data {send_full_data} to google")
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                print(f"Sending received data {data} to client")
                conn.send(data)
            conn.close()

if __name__ == "__main__":
    main()