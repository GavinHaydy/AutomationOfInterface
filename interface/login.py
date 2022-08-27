import requests
from common.get_keyword import GetKeyword
from config.glo_vars import url_glo

def token():
    res = requests.post( f'{url_glo()}/api/user/login',json={'phone': 'xxx', 'password': '2d3383fa392936ad7847c50a0bb4a58e'})
    result = GetKeyword()
    return result.get_keyword(res.json(), 'token')
