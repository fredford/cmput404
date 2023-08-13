#!/usr/bin/env python3

# Code modified from lab instruction

import os
import json
import cgi
import cgitb

cgitb.enable()

# Print all environment variables in plain text

#print("Content-Type: text/plain")
#print()
#print(os.environ)

# Print all environment variables in JSON

#print("Content-Type: application/json")
#print()
#print(json.dumps(dict(os.environ), indent=2))

# Print query parameter data in HTML

print("Content-Type: text/html")
print()

# Print query string
if "QUERY_STRING" in os.environ:
    print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# Print web browser information
if "HTTP_USER_AGENT" in os.environ:
    print(f"<p>BROWSER={os.environ['HTTP_USER_AGENT']}</p>")

print("""
<html>
<body>
""")
print("<ul>")
print(f"Key = Value")
for parameter in os.environ['QUERY_STRING'].split('&'):
    (name, value) = parameter.split('=')
    print(f"<li><em>{name}</em> = {value}</li>")
print("</ul>")

print("""
</body>
</html>
""")