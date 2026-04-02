from flask import Flask
from http import HTTPStatus
import json
import logging
import os
import yaml
from dotenv import load_dotenv

app = Flask(__name__)
cwd = os.getcwd()

# Logger configuration
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Using 2 different ways of externalizing settings for learning purposes
config = yaml.safe_load(open(f"{cwd}/config.yml"))
allowed_directories = config["Permission"]["directories"]

load_dotenv()
allowed_dir_env = os.getenv("ALLOWED_DIR")

@app.route("/", methods = ["GET"])# API response for successful startup
def home():
    logging.info("User requested: /")
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return json.dumps({"message":"Server is running."})

@app.route("/<dir_name>", methods = ["GET"])# API response for listing directory content
def get_dir(dir_name):
    dir_path = os.path.join(cwd, dir_name)
    if os.path.isdir(dir_path):
        if dir_name in allowed_directories:
            list_dict = dict()
            list_dict["Files"] = os.listdir(dir_path)
            logging.info("User requested: %s", dir_name)
            logging.info("Request successful, code: %d", HTTPStatus.OK.value)
            return json.dumps(list_dict)
        else:
            logging.info("User requested: %s", dir_name)
            logging.warning("Request unsuccessful, code: %d", HTTPStatus.FORBIDDEN.value)
            return json.dumps({"Error message": "No permission"}), HTTPStatus.FORBIDDEN.value
    else:
        logging.info("User requested: %s", dir_name)
        logging.warning("Request unsuccessful, code: %d", HTTPStatus.NOT_FOUND.value)
        return json.dumps({"Error message": "Directory not found"}), HTTPStatus.NOT_FOUND.value

@app.route("/<dir_name>/<filename>", methods = ["GET"])# API response for listing file content
def get_file(dir_name, filename):
    file_path = os.path.join(cwd, dir_name, filename)
    dir_path = os.path.join(cwd, dir_name)
    if os.path.isdir(dir_path):
        if dir_name in allowed_directories:
            if os.path.isfile(file_path):
                file_dict = dict()
                file_dict["filename"] = filename
                with open(file_path, "r") as file:
                    content = file.readlines()
                    file.close()
                file_dict["content"] = str(content)
                logging.info("User requested: %s", dir_name)
                logging.info("Request successful, code: %d", HTTPStatus.OK.value)
                return json.dumps(file_dict)
            else:
                logging.info("User requested: %s", filename)
                logging.warning("Request unsuccessful, code: %d", HTTPStatus.NOT_FOUND.value)
                return json.dumps({"Error message": "File not found."}), HTTPStatus.NOT_FOUND.value
        else:
            logging.info("User requested: %s", dir_name)
            logging.warning("Request unsuccessful, code: %d", HTTPStatus.FORBIDDEN.value)
            return json.dumps({"Error message": "No permission"}), HTTPStatus.FORBIDDEN.value
    else:
        logging.info("User requested: %s", dir_name)
        logging.warning("Request unsuccessful, code: %d", HTTPStatus.NOT_FOUND.value)
        return json.dumps({"Error message": "Directory not found"}), HTTPStatus.NOT_FOUND.value


if __name__ == "__main__":# Server startup
    HOST = "localhost"
    PORT = 8000
    app.run(host=HOST, port=PORT, debug=True)


