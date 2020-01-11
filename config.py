import random
import string

MAIN_API = 'http://localhost:8075'
MAIN_API = 'http://13.95.164.157:80'
USERMANAGER = '/auth'
USERMANAGER = '/usermanager'
COACHMANAGER = '/coachmanager'


def random_email_prefix():
    random.seed()
    email_prefix = random.randint(0, 100)
    return str(email_prefix) + random.choice(string.ascii_letters)


USEREMAIL = random_email_prefix() + '@email.email'
PASSWORD = 'password'
