from flask import Flask
from flask import request
import json
import os
import yaml
from dotenv import load_dotenv

app = Flask(__name__)
cwd = os.getcwd()

# Using 2 different ways of externalizing settings for learning purposes
config = yaml.safe_load(open(f"{cwd}/config.yml"))
allowed_directories = config["Permission"]["directories"]

load_dotenv()
allowed_dir_env = os.getenv("ALLOWED_DIR")

@app.route("/", methods = ["GET"])# API response for successful startup
def home():
    return json.dumps({"message":"Server is running."})

@app.route("/<dir_name>", methods = ["GET"])# API response for listing directory content
def get_dir(dir_name):
    dir_path = cwd + "/" + dir_name
    if os.path.isdir(dir_path):
        if dir_name in allowed_directories:
            list_dict = dict()
            list_dict["Files"] = os.listdir(dir_path)
            return json.dumps(list_dict)
        else:
            return json.dumps({"Error message": "No permission"})
    else:
        return json.dumps({"Error message": "Directory not found"})

@app.route("/<dir_name>/<filename>", methods = ["GET"])# API response for listing file content
def get_file(dir_name, filename):
    file_path = cwd + "/" + dir_name + "/" + filename
    dir_path = cwd + "/" + dir_name
    if os.path.isdir(dir_path):
        if dir_name in allowed_directories:
            if os.path.isfile(file_path):
                file_dict = dict()
                file_dict["filename"] = filename
                with open(file_path, "r") as file:
                    content = file.readlines()
                    file.close()
                file_dict["content"] = str(content)
                return json.dumps(file_dict)
            else:
                return json.dumps({"Error message": "File not found."})
        else:
            return json.dumps({"Error message": "No permission"})
    else:
        return json.dumps({"Error message": "Directory not found"})


if __name__ == "__main__":# Server startup
    HOST = "localhost"
    PORT = 8000
    app.run(host=HOST, port=PORT, debug=True)


