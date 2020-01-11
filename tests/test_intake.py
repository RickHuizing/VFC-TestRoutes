import json

from src import auth, intake

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg3NDY3NjQsIm5iZiI6MTU3ODc0Njc2NCwianRpIjoiZTBiNzBkYmItN2MyYy00MWVmLTg4N2YtNDk3ZDZlM2Q0MmYxIiwiZXhwIjoxNTc4NzQ3NjY0LCJpZGVudGl0eSI6OTAsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.kAZ0wMijTLVeITpIfbSDxJH7WqE0LhN6TbPTRCZjxmU'
refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg2ODExMjYsIm5iZiI6MTU3ODY4MTEyNiwianRpIjoiZTQzNGUzNzEtOWE4OS00N2MxLTk1NWMtZGUzZGVkNzE5N2JhIiwiaWRlbnRpdHkiOjkwLCJ0eXBlIjoicmVmcmVzaCJ9.lRUxXkECFTsGmeAgPkimqjhmgCjv_gnvyTbNsLKc1JY'
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