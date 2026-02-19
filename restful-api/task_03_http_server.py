#!/usr/bin/python3
"""
Docstring: http.server
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    """
    Docstring: Server class
    """

    def do_GET(self):
        """
        Doctring Method do_Get: This merthod
        hand requests GET
        """
        if self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
                }

            self.send_response(200)
            self.send_headers('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.data.encode('utf-8'))
            json = json.dumps(data)
            return
        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
            return

        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(file_to_open.encode())

        except Exception:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("404 Not Found".encode())


server_address = ('', 8000)
httpd = HTTPServer(server_address, Server)
print("Serving static content on port 8000")
httpd.serve_forever()
