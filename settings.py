from dotenv import load_dotenv
import logging
import os
import sys

from database import Database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("record.log"),
        logging.StreamHandler()
    ]
)

load_dotenv()

try:
    HOST = os.environ["HOST"]
    DATABASE = os.environ["POSTGRES_DB"]
    USERNAME = os.environ["POSTGRES_USER"]
    PASSWORD = os.environ["POSTGRES_PASSWORD"]
    APP_TOKEN = os.environ["APP_TOKEN"]
    APP_USERNAME = os.environ["APP_USERNAME"]
    APP_PASSWORD = os.environ["APP_PASSWORD"]
except KeyError as e:
    logging.exception(e)
    sys.exit(1)

DB_CONF = {
    'host': HOST,
    'database': DATABASE,
    'username': USERNAME,
    'password': PASSWORD,
}

db_handler = Database(**DB_CONF)

DATA_BASE_URL = "analisi.transparenciacatalunya.cat"
ENDPOINT = "irki-p3c7"
