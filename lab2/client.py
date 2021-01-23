#!/usr/bin/env python3

# Code modified from lab presentation

import socket, sys

# Create a tcp socket
def create_tcp_socket():
    print('Creating socket')

    # Try creating an IPv4 socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # If an error occurs output the failure code and message
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    
    # Return the socket created
    return s

# Get host IP from name
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()
    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

# Send data to server
def send_data(serversocket, payload):
    print("Sending payload")    
    
    # Send the encoded payload to the provided server socket
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")

def main():

    # Try creating a socket with Google, and sending a payload and receive the returned data
    try:
        # Define address info, payload, and buffer size
        host = 'www.google.com'
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096

        # Make the socket, get the ip, and connect
        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip , port))
        print (f'Socket Connected to {host} on ip {remote_ip}')
        
        # Send the data and shutdown
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        # Continue accepting data until no more left
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                 break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        # Always close at the end!
        s.close()
if __name__ == "__main__":
    main()
