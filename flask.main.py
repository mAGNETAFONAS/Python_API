from flask import Flask
from flask import request
import json
import os
app = Flask(__name__)
cwd = os.getcwd()

@app.route("/", methods = ["GET"])# API response for successful startup
def home():
    return json.dumps({"message":"Server is running."})

@app.route("/<dir_name>", methods = ["GET"])# API response for listing directory content
def files(dir_name):
    allowed_directories = ["files"]
    if os.path.isdir(cwd + request.path):
        if dir_name in allowed_directories:
            list_dict = dict()
            list_dict["Files"] = os.listdir(cwd + request.path)
            return json.dumps(list_dict)
        else:
            return json.dumps({"Error message": "No permission"})
    else:
        return json.dumps({"Error message": "Directory not found"})

@app.route("/files/<filename>", methods = ["GET"])# API response for listing file content
def file(filename):
    if os.path.isfile(cwd + request.path):
        file_dict = dict()
        file_dict["filename"] = filename
        file_path = cwd + request.path
        with open(file_path, "r") as file:
            content = file.readlines()
            file.close()
        file_dict["content"] = str(content)
        return json.dumps(file_dict)
    else:
        return json.dumps({"Error message": "File not found."})


if __name__ == "__main__":# Server startup
    HOST = "localhost"
    PORT = 8000
    app.run(host=HOST, port=PORT, debug=True)


