import json

import requests

BASE_URL = 'http://127.0.0.1:8000/bot-api/'


def create_user(user_id, name, username):
    url = f'{BASE_URL}users/'
    data = requests.get(url=url).json()
    user_exist = False
    for i in data:
        if i['user_id'] == user_id:
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={'username': username, 'name': name, 'user_id': user_id})
        return 'Foydalanivchi yaratildi.'
    else:
        return 'Foydalanivchi mavjud.'


