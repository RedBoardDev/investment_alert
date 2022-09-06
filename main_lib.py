import requests
from datetime import datetime, timedelta


def request_json(url):
    try:
        rsp = requests.get(url)
    except requests.exceptions.ConnectionError:
        return (None)
    return(rsp.json())

def get_yesterday_date():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')

def get_localtime():
    current_time = datetime.now()
    return (current_time)
