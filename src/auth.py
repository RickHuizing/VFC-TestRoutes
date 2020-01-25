import config
from config import MAIN_API, USERMANAGER
import requests

access_token = None
refresh_token = None


def get_headers(token):
    return {
        'Authorization': 'Bearer ' + str(token)
    }


def signup(email, password):
    r = requests.post(MAIN_API + USERMANAGER + '/signup', json={
        'name': 'testuser',
        'email': email,
        'password': password,
        'password_confirmation': config.PASSWORD
    })
    if r.status_code == 200:
        return True
    print(r.status_code, r.content)
    return False


def register():
    r = requests.post(MAIN_API + USERMANAGER + '/signup', json={
        'name': 'testuser',
        'email': config.USEREMAIL,
        'password': config.PASSWORD,
        'password_confirmation': config.PASSWORD
    })
    if r.status_code == 200:
        return True
    print(r.status_code, r.content)
    return False


def login(email=config.USEREMAIL, password=config.PASSWORD):
    global access_token, refresh_token
    r = requests.post(MAIN_API + USERMANAGER + '/login', json={
        'email': email,
        'password': password
    })
    if r.status_code == 200:
        data = r.json()
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        return access_token, refresh_token
    print(r.content)
    return None, None


def refresh_access_token(refr_token=refresh_token):
    global access_token
    r = requests.get(MAIN_API + USERMANAGER + '/refresh-token', headers=get_headers(refr_token))
    if r.status_code == 200:
        data = r.json()
        access_token = data['access_token']
        return access_token
    print('refreshing failed')
    print(r.status_code, r.content)
    return None
