import config
from src import auth


def register():
    if auth.register():
        print('registered')
        access_token, refresh_token = auth.login()
        if access_token:
            print('logged in')
            print(config.USEREMAIL)
            print('access_token:', access_token)
            print('refresh_token:', refresh_token)
            return access_token, refresh_token
    return None, None


if __name__ == "__main__":
    register()
