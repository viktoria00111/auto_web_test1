# отправка поста

import requests
import yaml


S = requests.Session()

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    url = data['url2']


def test_post(user_login):
    print(S.post(url=url, headers={'X-Auth-Token': user_login}, data={'title': data['title'], 'description': data['description'], 'content': data['content']}).json())