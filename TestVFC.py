from src import auth, intake, rating
from config import USEREMAIL

print('running tests for ' + USEREMAIL)

registered = auth.register()
if not registered:
    exit()
print('registered successful')

ACCESS, REFRESH = auth.login()
if ACCESS is None:
    exit()
print('logged in successful')

questions = intake.get_questions(ACCESS)
if questions:
    print('fetched questions successfully')
    print(questions)

ACCESS = auth.refresh_access_token()
if ACCESS is None:
    exit()
print('successfully refreshed access token')

if not intake.post_answers(ACCESS):
    exit()
print('saved answers succesfully')

if rating.rate_intervention(ACCESS):
    print('saved intervention response successfully')
