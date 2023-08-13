#!/usr/bin/env python3
# coding: utf-8
# Copyright 2016 Abram Hindle, https://github.com/tywtyw2002, and https://github.com/treedust
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it

import sys
import socket
import re
# you may use urllib to encode data appropriately
import urllib.parse

def help():
    print("httpclient.py [GET/POST] [URL]\n")

class HTTPResponse(object):
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    #def get_host_port(self,url):

    def connect(self, host, port):
        '''
        This method creates a socket connection to a provided host and port. Return the host if a connection is completed.
        '''
        # Set a port if it isn't specified
        if port == None:
            port = 80
        # Try connecting to the host:port
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
            print("Connected to %s:%s" % (host,port))
        # Exit if the connection is not made
        except:
            print("Could not connect to %s:%s" % (host,port))
            sys.exit(1)
        
        return host

    def get_code(self, data):
        '''
        This method returns the status code as an integer from the received data.
        '''
        return int(data.split()[1])

    def get_headers(self,data):
        '''
        This method was not used.
        '''
        return None

    def get_body(self, data):
        '''
        This method splits the body from the received data.
        '''
        return data.split("\r\n\r\n")[1]
    
    def sendall(self, data):
        '''
        This method sends the encoded request to the server.
        '''
        try:
            self.socket.sendall(data.encode('utf-8'))
        except:
            print("Unable to send.")
            sys.exit(1)
        
    def close(self):
        '''
        This method closes the socket
        '''
        self.socket.close()

    def recvall(self, sock):
        '''
        This method receives all data from the provided socket and returns the decoded data.
        '''
        buffer = bytearray()
        done = False
        while not done:
            try:
                part = sock.recv(1024)
            except:
                print("Unable to receive.")
                sys.exit(1)

            if (part):
                buffer.extend(part)
            else:
                done = not part
        return buffer.decode('utf-8')

    def GET(self, url, args=None):
        '''
        This method performs a GET request to the specified url with the arguments provided. Sends the request, receives the returned data and returns an HTTPResponse with the status code and body.
        '''
        code = 500
        body = ""

        # Parse the provided URL
        parsed_url = urllib.parse.urlparse(url)
        # Connect to the host:port
        host = self.connect(parsed_url.hostname, parsed_url.port)
        # Get the path specified from the URL
        path = parsed_url.path
        # If no path is set, use a the root path
        if path == "":
            path = "/"

        # Send a GET request through the open connection with the path and host specified
        self.sendall(f"""GET {path} HTTP/1.1\r\nHost: {host}\r\nAccept-Charset: utf-8\r\nConnection: close\r\n\r\n""")
        # Receive all data returned from the socket
        data = self.recvall(self.socket)
        # Get the status code from the received data
        code = self.get_code(data)
        # Get the body from the received data
        body = self.get_body(data)
        # Close the connection
        self.close()

        # Output the status code
        print(f"Status: {code}")
        # Output the body
        print(f"Body:\n{body}")

        return HTTPResponse(code, body)

    def POST(self, url, args=None):
        '''
        This method performs a POST request to the specified url with the arguments provided. Sends the request, receives the returned data and returns an HTTPResponse with the status code and body.
        '''
        code = 500
        body = ""

        # Parse the provided url
        parsed_url = urllib.parse.urlparse(url)
        # If no argument is provided set the query string to empty or encode the arguments
        if args == None:
            query_string = ""
        else:
            query_string = urllib.parse.urlencode(args)

        # Connect to the host:port
        host = self.connect(parsed_url.hostname, parsed_url.port)
        # Get the path specified from the URL
        path = parsed_url.path
        # Send a POST request through the open connection with the path and host specified, along with the query string and string length
        self.sendall(f"""POST {path} HTTP/1.1\r\nHost: {host}\r\nAccept-Charset: utf-8\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(query_string)}\r\nConnection: close\r\n\r\n{query_string}""")
        # Receive all data returned from the socket
        data = self.recvall(self.socket)
        # Get the status code from the received data
        code = self.get_code(data)
        # Get the body from the received data
        body = self.get_body(data)
        # Close the connection
        self.close()

        # Output the status code
        print(f"Status: {code}")
        # Output the body
        print(f"Body:\n{body}")

        return HTTPResponse(code, body)

    def command(self, url, command="GET", args=None):
        if (command == "POST"):
            return self.POST( url, args )
        else:
            return self.GET( url, args )
    
if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        print(client.command( sys.argv[2], sys.argv[1] ))
    else:
        print(client.command( sys.argv[1] ))
