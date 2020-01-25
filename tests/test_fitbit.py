import json

from src import auth, fitbit

access_token = ''
refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzk2OTY2NjUsIm5iZiI6MTU3OTY5NjY2NSwianRpIjoiNDE3ZDBlOTUtNTUxNy00NDdiLWI5NmUtMGJhMDhlNTJhNTczIiwiaWRlbnRpdHkiOjEwNiwidHlwZSI6InJlZnJlc2gifQ.qY6lnnUJnY-CeM0eAtG6K4tw7tkiX9XoKy1klb-V85s'


response: dict = fitbit.get_url(access_token)
if response is None:
    access_token = auth.refresh_access_token(refresh_token)
    response: dict = fitbit.get_url(access_token)
    if response is None:
        exit()
    print(access_token)
print('keys:', response.keys())
print('data:', response)

response = fitbit.test_authorization(access_token)
if response is not None:
    print(response)
response = fitbit.get_steps(access_token)
if response is None:
    exit()
print('keys:', response.keys())
print(response)
print('activities-steps:', json.dumps(response['activities-steps'], indent=1))
print('activities-steps-intraday:', response['activities-steps-intraday'])
