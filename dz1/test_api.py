# получение постов

import requests
import yaml


S = requests.Session()

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    url = data['url2']


def test_rest(user_login):
    print(S.get(url=url, headers={'X-Auth-Token': user_login}).json())