# Token test

import requests
import yaml


with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, url = data['username'], data['password'], data['url']


S = requests.Session()


def user_login():
    rest = S.post(url=url, data={'username': username, 'password': password})
    return rest.json()['token']


print(user_login())