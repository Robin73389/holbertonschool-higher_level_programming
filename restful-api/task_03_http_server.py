#!/usr/bin/python3


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

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
            return

        if self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))
            return

        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
            return

        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Endpoint not found".encode('utf-8'))


server_address = ('', 8000)
httpd = HTTPServer(server_address, Server)
print("Serving static content on port 8000")
httpd.serve_forever()
