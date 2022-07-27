import argparse

from models import Base
from settings import db_handler, logging


def init_db(reset_db=False):
    if reset_db:
        logging.warning('Deleting old database')
        Base.metadata.drop_all(db_handler.engine)
    Base.metadata.create_all(db_handler.engine)
    logging.info("Database updated")


if __name__ == "__main__":
    description = "Init Covid-19 vaccine dose database configuration"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--reset", action=argparse.BooleanOptionalAction, help="Reset database")
    args = parser.parse_args()
    try:
        init_db(reset_db=args.reset)
    except Exception as e:
        logging.exception(e)
