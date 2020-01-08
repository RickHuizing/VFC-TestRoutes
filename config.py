import random
import string

MAIN_API = 'http://localhost:8075'
USERMANAGER = '/auth'
COACHMANAGER = '/coachmanager'


def random_email_prefix():
    random.seed()
    email_prefix = random.randint(0, 100)
    return str(email_prefix) + random.choice(string.ascii_letters)


USEREMAIL = random_email_prefix() + '@email.email'
PASSWORD = 'password'
