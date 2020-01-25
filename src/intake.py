import random
import requests

from config import MAIN_API, COACHMANAGER
from src.auth import get_headers


def get_questions(access_token):
    r = requests.get(MAIN_API + COACHMANAGER + '/questions', headers=get_headers(access_token))
    if r.status_code == 200:
        return r.json()
    print('failed to get questions', r.status_code)
    return None


def post_answers(answers, access_token):
    r = requests.post(MAIN_API + COACHMANAGER + '/answers', headers=get_headers(access_token), json=answers)
    if r.status_code == 200:
        return True
    print('failed to save answers')
    return False


def build_answers_from_response(response):
    question_types = response['question_types']

    u_answers = {}
    for section_id, section in response['questions'].items():
        section_answers = {}
        for question in section:
            question_id = question['id']
            question_type = str(question['type'])
            question_type_str = question_types[question_type]
            if question_type_str == '':
                question_answers = [qu['value'] for qu in question['answers']]
            elif question_type_str in ['mc', 'cb', 'mc_statement', 'loss_choice']:
                question_answers = [qu['value'] for qu in question['answers']]
            elif question_type_str == 'open':
                question_answers = [random.randint(10, 150) for _ in range(5)]
            elif question_type_str in ['range', 'reactance_range']:
                question_answers = [random.randint(1, 5)]
            else:
                raise Exception('invalid question type found: ' + str(question_type))

            if question_type_str == 'cb':
                section_answers[question_id] = random.sample(question_answers, random.randint(1, len(question_answers)-1))
            else:
                section_answers[question_id] = random.choice(question_answers)

        u_answers[section_id] = section_answers
    u_ratings = {}
    for item_id, item_action in response['items'].items():
        u_ratings[item_id] = random.randint(1, 5)
    return {'ratings': u_ratings, 'answers': u_answers}
