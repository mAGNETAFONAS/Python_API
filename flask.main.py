from flask import Flask, render_template, request
from http import HTTPStatus
import logging
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
import mysql.connector
import yaml

app = Flask(__name__)
cwd = os.getcwd()

# Externalizing settings using config file and environment variables
config = yaml.safe_load(open(f"{cwd}/config.yml"))

class Configuration(BaseSettings):
    mysql_database: str = config["Database"]["name"]
    mysql_user: str = config["Database"]["user"]
    mysql_password: str = config["Database"]["password"]

    allowed_dir: list = config["Permission"]["directories"]
    network_host:  str = config["Network"]["Host"]
    network_port:  int = config["Network"]["Port"]
    server_debug: bool = config["Server settings"]["Debug"]

    logger_level: str = config["Logger"]["Level"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

config_class = Configuration()

# Logger configuration
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
logger.setLevel(config_class.logger_level.upper())

#Connection to MySQL database
mydb = mysql.connector.connect(
    host="python_api_db",
    user=config_class.mysql_user,
    password=config_class.mysql_password,
    database=config_class.mysql_database
)
mycursor = mydb.cursor(buffered=True)

@app.route("/", methods = ["GET"])# API response for successful startup
def intro():
    logging.info("User requested: /")
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("intro.html")

@app.route("/web/", methods = ["GET"])# API response for successful startup
def home():
    logging.info("User requested: /web/")
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("index.html")

@app.route("/web/<dir_name>", methods = ["GET"])# API response for listing directory content
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

@app.route("/web/<dir_name>/<filename>", methods = ["GET"])# API response for listing file content
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


@app.route("/db/", methods = ["GET", "POST"])# API response for selecting Database service
def db_home():
    logging.info("User requested: /db/")
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("db.html")

@app.route("/db/create", methods = ["GET", "POST"])# API response for creating a new user in a database
def db_create():
    logging.info("User requested: /db/create")
    if request.method == "POST":
        print("veik")
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")
        address = request.form.get("address")
        telephone_num = request.form.get("telephone_num")
        sql = "INSERT INTO users (name, surname, email, password, address, telephone_num) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (name, surname, email, password, address, telephone_num)
        mycursor.execute(sql, val)
        mydb.commit()
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("create.html")

@app.route("/db/list_all", methods = ["GET", "POST"])# API response for listing all users in a database
def db_list_all():
    logging.info("User requested: /db/list_all")
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    mydb.commit()
    result = mycursor.fetchall()
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("db.html", rows=result)

@app.route("/db/list_<id_num>", methods = ["GET", "POST"])# API response for listing a specific user in a database
def db_list_id(id_num):
    logging.info(f"User requested: /db/list_{id_num}")
    sql = "SELECT * FROM users WHERE id = %s"
    mycursor.execute(sql, (id_num,))
    mydb.commit()
    result = mycursor.fetchall()
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("db.html", rows=result)

@app.route("/db/delete_<id_num>", methods = ["GET", "POST"])# API response for deleting a specific user in a database
def db_delete(id_num):
    logging.info(f"User requested: /db/delete_{id_num}")
    sql = "DELETE FROM users WHERE id = %s"
    mycursor.execute(sql, (id_num,))
    mydb.commit()
    logging.info("Request successful, code: %d", HTTPStatus.OK.value)
    return render_template("db.html", msg="User deleted successfully")

if __name__ == "__main__":# Server startup
    app.run(host=config_class.network_host, port=config_class.network_port, debug=config_class.server_debug)


