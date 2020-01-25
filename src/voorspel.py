import requests

from config import VOORSPELSERVICE


def make_model(user_id):
    json_data = {"user_id": user_id}
    r = requests.get(VOORSPELSERVICE + '/api/make_model', json=json_data)
    if r.status_code == 200:
        return r.json()
    print('failed to make model:', r.status_code, r.text)
    return False


def get_prediction(user_id, hour=20):
    json_data = {"user_id": user_id, 'hour': hour}
    r = requests.get(VOORSPELSERVICE + '/api/predict', json=json_data)
    if r.status_code == 200:
        return r.json()
    print('failed to get a prediction:', r.status_code, r.text)
    return False
