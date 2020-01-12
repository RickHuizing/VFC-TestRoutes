import requests

from config import *
r = requests.get(MAIN_API + '/')
print(r.status_code, r.content)
print(r)