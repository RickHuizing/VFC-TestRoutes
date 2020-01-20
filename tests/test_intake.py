import json
import random

import pandas
import requests

from src import auth, intake
from tests import generate_user

access_token, refresh_token = generate_user.register()

if access_token == '':
    print('enter fresh tokens')
    exit()

response: dict = intake.get_questions(access_token)
if response is None:
    access_token = auth.refresh_access_token(refresh_token)
    response: dict = intake.get_questions(access_token)
    if response is None:
        exit()
    print(access_token)

u_answers = intake.build_answers_from_response(response)

print('keys:', response.keys())
questions = response.pop('questions')
print(json.dumps(response, indent=1))
items = response['items']
sections = response['sections']
question_types = response['question_types']
print()

print('questions (by section):')
for section, questions in questions.items():
    print(section + ':')
    for question in questions:
        if section in ['4', '6']:
            print('   ', dict(sorted(question.items(), reverse=True)))
        else:
            answers = question.pop('answers')
            print(' ', dict(sorted(question.items(), reverse=True)))
            print(' ', "  'answers': [")
            for a in answers:
                print(' ', ' ', ' ', a)
            print(' ', "    ]")

# print(json.dumps(u_answers, indent=1))
print(intake.post_answers(u_answers, access_token))

userdata = 'http://localhost:8082'
GET_USERS = "/api/get_users"
users = requests.get(userdata + GET_USERS)
user_df = pandas.DataFrame.from_dict(users.json())
user_df = user_df.assign(db_id=user_df.id)
r = requests.get('http://localhost:8080/get_demographics', json={'users': user_df.to_json()})
user_df = pandas.DataFrame.from_dict(r.json())

print()