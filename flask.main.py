from flask import Flask, render_template
from http import HTTPStatus
import logging
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml


app = Flask(__name__)
cwd = os.getcwd()

# Logger configuration
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Using 2 different ways of externalizing settings for learning purposes
config = yaml.safe_load(open(f"{cwd}/config.yml"))

class Configuration(BaseSettings):
    allowed_dir: list = config["Permission"]["directories"]
    network_host:  str = config["Network"]["Host"]
    network_port:  int = config["Network"]["Port"]
    server_debug: bool = config["Server settings"]["Debug"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

config_class = Configuration()

@app.route("/", methods = ["GET"])# API response for successful startup
def home():
    logging.info("User requested: /")
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("index.html")

@app.route("/<dir_name>", methods = ["GET"])# API response for listing directory content
def get_dir(dir_name):
    logging.info("User requested: %s", dir_name)
    dir_path = os.path.join(cwd, dir_name)
    if os.path.isdir(dir_path):
        if dir_name in config_class.allowed_dir:
            list_dict = dict()
            try:
                list_dict["Files"] = os.listdir(dir_path)
            except Exception as ex:
                usr_err_msg = str(ex).split(":")[0]
                logging.warning(f"Error message: {ex}, code: %d", HTTPStatus.FORBIDDEN.value)
                return render_template("index.html", dir_list=usr_err_msg), HTTPStatus.FORBIDDEN.value
            logging.info("Request successful, code: %d", HTTPStatus.OK.value)
            return render_template("index.html", dir_list=list_dict["Files"])
        else:
            logging.warning("Request unsuccessful, code: %d", HTTPStatus.FORBIDDEN.value)
            return render_template("index.html", dir_list="No Permission"), HTTPStatus.FORBIDDEN.value
    else:
        logging.warning("Request unsuccessful, code: %d", HTTPStatus.NOT_FOUND.value)
        return render_template("index.html", dir_list="Directory not found"), HTTPStatus.NOT_FOUND.value

@app.route("/<dir_name>/<filename>", methods = ["GET"])# API response for listing file content
def get_file(dir_name, filename):
    logging.info("User requested: %s/%s", dir_name, filename)
    file_path = os.path.join(cwd, dir_name, filename)
    dir_path = os.path.join(cwd, dir_name)
    if os.path.isdir(dir_path):
        if dir_name in config_class.allowed_dir:
            if os.path.isfile(file_path):
                file_dict = dict()
                file_dict["filename"] = filename
                try:
                    with open(file_path, "r") as file:
                        content = file.readlines()
                        file.close()
                except Exception as ex:
                    usr_err_msg = str(ex).split(":")[0]
                    logging.warning(f"Error message: {ex}, code: %d", HTTPStatus.FORBIDDEN.value)
                    return render_template("index.html", dir_list=usr_err_msg), HTTPStatus.FORBIDDEN.value

                file_dict["content"] = str(content)
                logging.info("Request successful, code: %d", HTTPStatus.OK.value)
                return render_template("index.html", dir_list=file_dict["content"])
            else:
                logging.warning("Request unsuccessful, code: %d", HTTPStatus.NOT_FOUND.value)
                return render_template("index.html", dir_list="File not found"), HTTPStatus.NOT_FOUND.value
        else:
            logging.warning("Request unsuccessful, code: %d", HTTPStatus.FORBIDDEN.value)
            return render_template("index.html", dir_list="No Permission"), HTTPStatus.FORBIDDEN.value
    else:
        logging.warning("Request unsuccessful, code: %d", HTTPStatus.NOT_FOUND.value)
        return render_template("index.html", dir_list="Directory not found"), HTTPStatus.NOT_FOUND.value


if __name__ == "__main__":# Server startup
    app.run(host=config_class.network_host, port=config_class.network_port, debug=config_class.server_debug)


