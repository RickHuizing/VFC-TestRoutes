import requests

from config import MAIN_API, COACHMANAGER
from src.auth import get_headers


def get_questions(access_token):
    r = requests.get(MAIN_API + COACHMANAGER + '/get_questions', headers=get_headers(access_token))
    if r.status_code == 200:
        return r.json()
    print('failed to get questions', r.status_code)
    return None


def post_answers(access_token):
    answers = {
        "question_ids": "1,2, 5", "answers": "-1, 2, 3", "item_ids": "1,2,3", "ratings": "1,5,3"
    }
    r = requests.post(MAIN_API + COACHMANAGER + '/answers', headers=get_headers(access_token), json=answers)
    if r.status_code == 200:
        return True
    print('failed to save answers')
    return False
