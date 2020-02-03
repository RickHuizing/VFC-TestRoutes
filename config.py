import random
import string

MAIN_API = 'http://localhost:8075'
# MAIN_API = 'https://virtualcoachdev.cmi.hanze.nl'
USERMANAGER = '/auth'
COACHMANAGER = '/coachmanager'
TRACKERMANAGER = '/trackermanager'
VOORSPELSERVICE = 'http://localhost:8086'

def random_email_prefix():
    random.seed()
    email_prefix = random.randint(0, 100)
    return str(email_prefix) + random.choice(string.ascii_letters)


USEREMAIL = random_email_prefix() + '@email.email'
# USEREMAIL = 'admin1' + '@email.email'
PASSWORD = 'password'
