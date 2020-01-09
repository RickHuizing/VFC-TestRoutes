import random

import requests

from config import MAIN_API, COACHMANAGER
from src.auth import get_headers

locations = [('Groningen', 53.217351, 6.566286), ('Zuidwolde', 53.2597260, 6.5908420),
             ('De Hunze', 53.2425740, 6.5791261), ('Haren', 53.1704182, 6.6049075),
             ('Airport Eelde', 53.1222435, 6.5750545), ('Assen', 52.9925222, 6.5644169),
             ('Baggelhuizen', 52.9829118, 6.5335178), ('Marsdijk', 53.0208178, 6.5899944),
             ('Gieten', 53.0030860, 6.7627287), ('Alkmaar', 52.6413968, 4.7917557),
             ('Rotterdam', 51.9294481, 4.4848251), ('Maastricht', 50.8511495, 5.6874847),
             ('Aachen', 50.7794578, 6.0774994), ('Haarlem', 52.373029, 4.630103),
             ('Amsterdam', 52.3739486, 4.8925209), ('Amsterdam Nieuw-West', 52.3653935, 4.8034716),
             ('Anne Frank Huis', 52.3766340, 4.8632741)]


def save_location(access_token):
    location = random.choice(locations)
    data = {
        'longitude': location[1],
        'latitude': location[2],
    }
    r = requests.post(MAIN_API + COACHMANAGER + '/location', headers=get_headers(access_token), json=data)
    if r.status_code == 200:
        return True
    print('failed to save location', r.text)
    return False
