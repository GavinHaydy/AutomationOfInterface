"""
    @Author: GavinHaydy
    @Email: bugpz2779@gmail.com
    @CSDN: 'https://blog.csdn.net/BUGPZ'
"""

import requests
from common.get_keyword import GetKeyword
from common.conf import read_yaml


def token():
    data = ["username", "password"]
    login_pat = eval(f"{read_yaml('../config/env.yaml')['login']}")
    res = requests.request(login_pat['method'].lower(), login_pat['url'],
                           json={key: val for key, val in login_pat.items() if key in data}).json()
    return GetKeyword.get_keyword(res, login_pat['token_name'])
