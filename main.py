import json
import http.server
import os
import socketserver

cwd = os.getcwd()


class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request, client_address, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)

    def api_response_status(self):
        return "Server is running.".encode()

    def api_response_dir(self):
        return "files: ".encode() + str(os.listdir(cwd + self.path)).encode()

    def do_GET(self):
        if self.path == "/":
            print(self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/plain ")
            self.end_headers()
            self.wfile.write(self.api_response_status())

        if self.path == "/files":
            print(self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/plain ")
            self.end_headers()
            self.wfile.write(self.api_response_dir())

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    with socketserver.TCPServer((HOST, PORT), Handler) as server:
        print(f"Server started at {PORT}")
        server.serve_forever()
