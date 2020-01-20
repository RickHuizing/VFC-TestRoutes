import requests

from config import MAIN_API, TRACKERMANAGER
from src.auth import get_headers


def toggle_test(user_id):
    r = requests.get(MAIN_API + TRACKERMANAGER + '/fitbit/toggle', json={'user_id': user_id})
    if r.status_code == 200:
        return r.content
    print('failed to toggle test mode', r.status_code)
    print(r.content)
    return None


def get_url(access_token):
    r = requests.get(MAIN_API + TRACKERMANAGER + '/fitbit/get_url', headers=get_headers(access_token))
    if r.status_code == 200:
        return r.json()
    print('failed to get authorisation url', r.status_code)
    print(r.content)
    return None


def get_steps(access_token):
    r = requests.get(MAIN_API + TRACKERMANAGER + '/fitbit/get_steps', headers=get_headers(access_token))
    if r.status_code == 200:
        return r.json()
    print('failed to get steps', r.status_code)
    return None


def test_authorization(access_token):
    r = requests.get(MAIN_API + TRACKERMANAGER + '/fitbit/authorized', headers=get_headers(access_token))
    if r.status_code == 200:
        return r.json()
    print('failed to get authorization', r.status_code)
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
