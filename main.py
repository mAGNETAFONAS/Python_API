import json
import http.server
import os
import socketserver
import re

cwd = os.getcwd()
pattern = "\w"


class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request, client_address, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)

    def api_response_status(self):
        return "Server is running.".encode()

    def api_response_list(self):
        list_dict = {}
        list_dict["Files"] = os.listdir(cwd + self.path)
        return json.dumps(list_dict).encode()

    def api_response_file(self):
        file_dict = {}
        file_dict["filename"] = self.path.split("/")[1]
        file_path = cwd + self.path
        with open(file_path, "r") as file:
            content = file.readlines()
            file.close()
        file_dict["content"] = str(content)
        return json.dumps(file_dict).encode()

    def do_GET(self):
        if self.path == "/":
            print(self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(self.api_response_status())

        elif self.path == "/files":
            print(self.path)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(self.api_response_list())

        elif re.match(pattern, self.path.split("/")[1]) != None :
            print(self.path)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(self.api_response_file())
        print(self.path)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    with socketserver.TCPServer((HOST, PORT), Handler) as server:
        print(f"Server started at {PORT}")
        server.serve_forever()
