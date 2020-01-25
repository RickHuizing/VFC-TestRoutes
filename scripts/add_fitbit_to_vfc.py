import json

from src import auth, fitbit

# access_token = ''
# refresh_token = ''
email = 'vladimir@putin.ru'
password = 'specerijen'
auth.signup(email, password)
access_token, refresh_token = auth.login(email, password)

response: dict = fitbit.get_url(access_token)
if response is None:
    access_token = auth.refresh_access_token(refresh_token)
    response: dict = fitbit.get_url(access_token)
    if response is None:
        exit()
    print(access_token)
print('keys:', response.keys())
print('data:', response)

wait = input('enter id of user you just authorized')
user_id = int(wait)
# user_id = 30
print(fitbit.toggle_test(user_id))
