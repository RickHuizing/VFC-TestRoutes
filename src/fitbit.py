import requests

from config import MAIN_API, TRACKERMANAGER, USERMANAGER
from src.auth import get_headers


def get_url(access_token):
    r = requests.get(MAIN_API + TRACKERMANAGER + '/fitbit/get_url', headers=get_headers(access_token))
    if r.status_code == 200:
        return r.json()
    print('failed to get authorisation url', r.status_code)
    return None


def callback(access_token):
    answers = {
        'answers': {
            '1': 2, '2': 6, '5': 14
        },
        'ratings': {
            '1': 1, '2': 5, '3': 3
        }
    }
    r = requests.post(MAIN_API + TRACKERMANAGER + '/fitbit/callback')
    if r.status_code == 200:
        return True
    print('failed to authorise fitbit')
    return False
