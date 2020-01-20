import json
import time

from src import auth, fitbit
from tests.generate_user import register

# access_token, refresh_token = register()
# access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg5MzI5NjgsIm5iZiI6MTU3ODkzMjk2OCwianRpIjoiZTE0MzlmYjEtZDAxNS00ODM5LWFkNDYtMjBkMmE3NTgwNDI2IiwiZXhwIjoxNTc4OTMzODY4LCJpZGVudGl0eSI6MTQxMiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.ED1kEGQ4tAH4JIWoTrdyk06gLcS_4urcyAbmho40h0s'
# refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg5Mjg3MjEsIm5iZiI6MTU3ODkyODcyMSwianRpIjoiM2M4ZjhkYmQtMmEyNy00NzFlLWE0ZWItNWRlYTFhNTc5NzIzIiwiaWRlbnRpdHkiOjE0MTIsInR5cGUiOiJyZWZyZXNoIn0.ii6zQp96pk872ocoz9p3e_esv0WOiYvyYdNgns0iOKU'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg5NTQxNzMsIm5iZiI6MTU3ODk1NDE3MywianRpIjoiZDMxMzRjN2EtMGYwOS00MWFhLTkwMDYtZGE3OGFhNTkzNTNiIiwiZXhwIjoxNTc4OTU1MDczLCJpZGVudGl0eSI6MjA3MCwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.NIRYAESVRc5aL2ApP-Vg_58SYamzoeYYxaePkmNTplg'
refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg5NTQxNzMsIm5iZiI6MTU3ODk1NDE3MywianRpIjoiMWI2NjlmYTItMjJjNC00Y2ZmLTk2MTMtMzZjYjNkYzBhODZkIiwiaWRlbnRpdHkiOjIwNzAsInR5cGUiOiJyZWZyZXNoIn0.GK1BDdfyBKHYIV3AcD5oe-ZJUR44MG0R9A221Fc5DHI'


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
