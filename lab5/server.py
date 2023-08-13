#  coding: utf-8 
import socketserver
import os

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
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
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        # Receive request and clean sent data
        self.data = self.request.recv(1024).decode("utf-8")
        # Separate data headers by lines
        self.split_lines = self.data.splitlines()
        # Check that GET is the method
        if not self.split_lines[0].startswith("GET"):
            self.error_codes("405")
            return
        # Store header information
        self.data_headers = {}
        for x in self.data.splitlines():
            if not x.startswith("GET") and not x == "":
                key, value = x.split(": ")
                self.data_headers[key] = value
        # Prevent non-direct directory requests
        if ".." in self.split_lines[0]:
            self.error_codes("404")
            return
        # Get the requested path
        requested = self.split_lines[0].split(" ")[1]

        # Check if the path is a directory
        if os.path.isdir("www" + requested) and requested[-1] == "/":
            path = "www" + requested + "index.html"
        # Check if the path is a directory with an additional '/'
        elif os.path.isdir("www" + requested + "/"):
            self.error_codes("301", requested + "/")
            return
        # Check if the file is not valid
        elif not os.path.isfile("www" + requested):
            self.error_codes("404", requested)
            return
        # If a path is valid add the www directory
        else:
            path = "www" + requested

        html_file = ""
        # Read the data from the specified file
        file_data = open(path, 'r')
        for line in file_data:
            html_file += line
        # Send the file information
        self.request.sendall(bytearray("HTTP/1.1 200 OK\r\nContent-Type: text/%s; charset=utf-8\r\n\r\n"%(path.split(".")[1])+html_file, 'utf-8'))

    def error_codes(self, error, location=None):
        # This function handles error requests

        # Send information for a 301 Moved Permanently
        if error == "301":
            self.request.sendall(bytearray(f"""HTTP/1.1 301 Moved Permanently\r\nLocation: {location}\r\nContent-Type: text/plain; charset=utf-8\r\nStatus: 301 Moved Permanently\r\n\r\n301 Moved""", 'utf-8'))
        # Send information for a 404 Not Found
        elif error == "404":
            self.request.sendall(bytearray("""HTTP/1.1 404 Not Found
                                          \r\nContent-Type: text/html; charset=utf-8
                                          \r\nStatus: 404 Not Found\r\n
                                          \r\n<html>
                                              <head>
                                              <title>404 Not Found</title>
                                              </head>
                                              <body>
                                              <center>
                                              <h1>404 Not Found</h1>
                                              </center>
                                              </body>
                                              </html>
                                               """, 'utf-8'))
        # Send information for a 405 Method Not Allowed
        elif error == "405":
            self.request.sendall(bytearray("""HTTP/1.1 405 Method Not Allowed
                                          \r\nContent-Type: text/plain; charset=utf-8
                                          \r\nStatus: 405 Method Not Allowed\r\n\r\n""", 'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
