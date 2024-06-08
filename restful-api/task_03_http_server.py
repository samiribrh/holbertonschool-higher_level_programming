#!/usr/bin/python3
"""Module to implement http.server module"""
import http.server
import json


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """Simple Handler class inherited from BaseHTTPRequestHandler"""

    def _set_headers(self, status_code=200, content_type='text/plain'):
        """Method to set headers"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Method to handle GET requests"""

        # Base case
        if self.path == '/':
            self._set_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        # If /data is accessed
        elif self.path == '/data':
            self._set_headers(content_type='application/json')
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # /status endpoint
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == '/info':
            self._set_headers(content_type='application/json')
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Error 404 :)
        else:
            self.send_error(404, "Endpoint not found")
            self._set_headers(404, 'text/plain')
            self.wfile.write("404 Not Found: The requested resource was not found on this server.".encode('utf-8'))


if __name__ == '__main__':
    """Server initialization"""
    server_address = ('', 8000)
    httpserver = http.server.HTTPServer(server_address, HTTPHandler)
    httpserver.serve_forever()
