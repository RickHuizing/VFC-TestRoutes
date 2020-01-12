import time

from src import auth, fitbit
from tests.generate_user import register

access_token, refresh_token = register()
if access_token is None:
    print('server offline')
    exit()

response: dict = fitbit.get_url(access_token)
if response is None:
    access_token = auth.refresh_access_token(refresh_token)
    response: dict = fitbit.get_url(access_token)
    if response is None:
        exit()
    print(access_token)

print('keys:', response.keys())
print('data:', response)
