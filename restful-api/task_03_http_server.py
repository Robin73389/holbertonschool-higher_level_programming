#!/usr/bin/python3
"""
Docstring: http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


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
            self.end_headers('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
            json = json.dumps(data)
            return
        if self.path == '/status':
            self.send_reponse(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write()
            return

        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_header()
            self.wfile.write(file_to_open.encode())

        except Exception:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write()


server_address = ('', 8000)
httpd = HTTPServer(server_address, Server)
print("Serving static content on port 8000")
httpd.serve_forever()
