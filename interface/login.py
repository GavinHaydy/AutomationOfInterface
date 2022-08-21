import requests
from common.get_keyword import GetKeyword

def token():
    res = requests.post('http://xxx/api/user/login',json={'phone': 'xxx', 'password': '2d3383fa392936ad7847c50a0bb4a58e'})
    result = GetKeyword()
    return result.get_keyword(res.json(), 'token')
