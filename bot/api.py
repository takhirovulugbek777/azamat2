import json

import requests

BASE_URL = 'https://checkdevice.uz/bot-api/'


def create_user(user_id, name, username):
    url = f'{BASE_URL}users/'
    response = requests.post(url=url, data={'user_id': user_id, 'name': name, 'username': username})
    if response.status_code == 201:
        return 'Foydalanuvchi yaratildi'
    elif response.status_code == 200:
        return 'Foydalanuvchi mavjud'
    else:
        return 'Xatolik yuz berdi'
