import pytest
import yaml
import requests


with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, url = data['username'], data['password'], data['url']

S = requests.Session()


@pytest.fixture()
def user_login():
    rest = S.post(url=url, data={'username': username, 'password': password})
    return rest.json()['token']