import json

from src import auth, intake

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg4MzY4OTgsIm5iZiI6MTU3ODgzNjg5OCwianRpIjoiMTA3ZmFmOTMtM2VhOC00ODcxLWFlMzEtMzljNzcwZGE2NWVkIiwiZXhwIjoxNTc4ODM3Nzk4LCJpZGVudGl0eSI6MTA0NCwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.8nlB24xKOwsIEjyrIyK9UOD3UWJzJTZ48GIk9ExxpqI'
refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg4MzY4OTgsIm5iZiI6MTU3ODgzNjg5OCwianRpIjoiMWY1OWMyMDEtMTIyMy00MTI4LWIzODgtNDFiMjM5M2JiZGRlIiwiaWRlbnRpdHkiOjEwNDQsInR5cGUiOiJyZWZyZXNoIn0.yQcfxrW7v6-tTfF89Jn_ZlC7eL4IXi_EPiAMZU7IiA4'
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

print(intake.post_answers(access_token))