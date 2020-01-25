import requests
from datetime import datetime

start = datetime.now()
r = requests.get('http://localhost:8084/api/get_steps', json={'user_id': 1})
print('fetching steps took: ', datetime.now() - start)
