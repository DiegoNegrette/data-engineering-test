import argparse
import datetime

from api import get_this_week_data
from models import VaccineData
from settings import db_handler, logging
from utils import remove_repeated_dicts_from_list


def main(**kwargs):
    new_items_list = []
    db_handler.start_session()
    data_results = get_this_week_data(**kwargs)
    data_results = remove_repeated_dicts_from_list(data_results)
    total_records = len(data_results)
    logging.debug(f"{total_records} item(s) where found")
    for count, item in enumerate(data_results):
        logging.info(f"Processing {count+1}/{total_records} item(s)")
        try:
            date_time_obj = datetime.datetime.strptime(item["data"], "%Y-%m-%dT%H:%M:%S.%f")
            formatted_comarca = item["comarca"].title()
        except Exception as e:
            logging.exception(e)
            continue
        item_dict = {
            "comarca": formatted_comarca,
            "first_vaccine_doses": item["dosi"],
            "day": date_time_obj,
        }
        if db_handler.does_item_exist(VaccineData, **item_dict):
            logging.info(f"Item with {item_dict} already found on db")
            continue
        vaccine_data_obj = VaccineData(**item_dict)
        new_items_list.append(vaccine_data_obj)
        logging.info(f"Adding {vaccine_data_obj} to db")
    if new_items_list:
        db_handler.bulk_create_objs(new_items_list)
    db_handler.end_session()
    logging.info(f"Task Finished, {len(new_items_list)} new item(s) added")


if __name__ == "__main__":
    description = "Get Covid-19 vaccine dose daily data"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--limit", nargs='?', default=None, help="Limit results?")
    args = parser.parse_args()
    try:
        main(limit=args.limit)
    except Exception as e:
        logging.exception(e)
