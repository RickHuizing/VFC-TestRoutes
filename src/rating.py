import random

import requests

from config import MAIN_API, COACHMANAGER
from src.auth import get_headers


def rate_intervention(access_token):
    rating = {
        # item 1 is rated whenever a user is created while UserManager is running with dev mode enabled in config
        "rating": random.randint(1, 5), "item_id": 1, "successful": True
    }
    r = requests.post(MAIN_API + COACHMANAGER + '/intervention_response', headers=get_headers(access_token),
                      json=rating)
    if r.status_code == 200:
        return True
    print('failed to rate intervention', r.text)
    return False
