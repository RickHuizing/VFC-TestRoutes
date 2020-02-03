import json

from src import auth, fitbit

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODAyMTMwNDYsIm5iZiI6MTU4MDIxMzA0NiwianRpIjoiMThhY2Y3MmQtMWY0Zi00NzExLWI1MzgtZTg0OGNmMmE1MmY2IiwiaWRlbnRpdHkiOjExNCwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.Gb3QxnLWiYYBM32iAmGzk8ujlasE1JSFamqWBbLbnIk'
refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODAyMTI5NDgsIm5iZiI6MTU4MDIxMjk0OCwianRpIjoiYzczOTBmYWYtNDVhMi00MGI3LTg4YWMtOGU0MjhlODgzMGUyIiwiaWRlbnRpdHkiOjExMywidHlwZSI6InJlZnJlc2gifQ.oP4jAfyK1nLP1vAO7Xxz43XkSaK1HfJVZQBdAf-FGc8'

response: dict = fitbit.get_url(access_token)
if response is None:
    access_token = auth.refresh_access_token(refresh_token)
    response: dict = fitbit.get_url(access_token)
    if response is None:
        exit()
    print(access_token)
print('keys:', response.keys())
print('data:', response)
input('please register fitbit through url or quit this program, enter any symbol to continue')

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
