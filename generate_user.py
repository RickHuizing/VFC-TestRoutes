import config
from src import auth

if auth.register():
    print('registered')
    access_token, refresh_token = auth.login()
    if access_token:
        print('logged in')
        print(config.USEREMAIL)
        print(access_token)
        print(refresh_token)
