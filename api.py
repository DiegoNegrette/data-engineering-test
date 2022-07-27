import datetime
from sodapy import Socrata

from settings import APP_TOKEN, APP_PASSWORD, APP_USERNAME, DATA_BASE_URL, ENDPOINT
from utils import format_datetime_obj


def _get_data_between_dates(start_date, end_date, **kwargs):
    start_date = format_datetime_obj(start_date)
    end_date = format_datetime_obj(end_date)
    limit = kwargs.get('limit', 2000)
    client = Socrata(
        DATA_BASE_URL, APP_TOKEN,
        username=APP_USERNAME,
        password=APP_PASSWORD
    )
    data_results = client.get(ENDPOINT, where=f"data >= '{start_date}' and data < '{end_date}'", order="data", limit=limit, select="comarca, data, dosi")
    return data_results


def _get_weekly_data_by_date(date, **kwargs):
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    return _get_data_between_dates(start_week, end_week, **kwargs)


def _get_daily_data_by_date(date, **kwargs):
    start_day = datetime.datetime(date.year, date.month, date.day)
    end_day = start_day + datetime.timedelta(1)
    return _get_data_between_dates(start_day, end_day, **kwargs)


def get_this_week_data(**kwargs):
    date = datetime.date.today()
    return _get_weekly_data_by_date(date, **kwargs)


def get_current_day_data(**kwargs):
    date = datetime.date.today()
    return _get_daily_data_by_date(date, **kwargs)
