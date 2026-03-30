import json
import http.server
import socketserver



class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request, client_address, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)

    def api_response(self):
        return "Server is running.".encode()

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "string")
            self.end_headers()
            self.wfile.write(self.api_response())

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    with socketserver.TCPServer((HOST, PORT), Handler) as server:
        print(f"Server started at {PORT}")
        server.serve_forever()
