"""
    @Author: GavinHaydy
    @Email: bugpz2779@gmail.com
    @CSDN: 'https://blog.csdn.net/BUGPZ'
"""
import json.decoder
import re
from urllib.parse import urlparse
from requests import request
from pre_operation.login import token
from common.conf import read_yaml
from common.get_keyword import GetKeyword


def _get_config():
    conf = read_yaml('config/send_method.yaml')
    return conf


class Foo:
    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if hasattr(attr, '__call__'):
            def new_func(*args, **kwargs):
                # 获取完整api路径
                path = urlparse(args[1]).path

                # 白名单处理 Authorization根据实际情况修改，后续改为配置项
                white_list = _get_config()['whiteList']
                for i in white_list:
                    if i == path:
                        return attr(*args, **kwargs)
                    if i.find('*') != -1:
                        pat = i.replace('*', '(.*?)')
                        if re.search(pat, path):
                            return attr(*args, **kwargs)

                # 判断header是否存在token 没有则调用token
                print('before calling %s' % attr.__name__)
                if kwargs.get('headers'):
                    if kwargs.get('headers').get(_get_config()['tokenConf']['token_name']) is None:
                        result = attr(*args, **kwargs)
                        print('done calling %s' % attr.__name__)
                        return result
                else:
                    headers = dict()
                    headers[_get_config()['tokenConf']['token_name']] = _get_config()['tokenConf']['token_prefix'] + token()
                    kwargs.setdefault('headers', headers)
                    return attr(*args, **kwargs)

            return new_func
        else:
            return attr


class SendMethod(Foo):
    @staticmethod
    def send_method(method, url, **kwargs):
        """
        :param method: 请求方式
        :param url: 请求地址
        :return: 请求结果dict
        """
        default_method = ['get', 'post', 'head', 'put', 'delete', 'patch', 'options']
        if method.lower() in default_method:
            response = request(method.lower(), url, **kwargs)
        else:
            raise ValueError(f'The request mode {method} is not supported')
        result = dict()

        result['req'] = response.request  # 请求体
        try:
            result['rsp'] = response.json()  # 响应体
            msg_key = _get_config()['apiError']['msg_key']
            code_key = _get_config()['apiError']['code_key']
            error_msg = _get_config()['apiError']['value']
            error_code = _get_config()['apiError']['code']

            # 判断token是否过期，过期则重走登录
            if GetKeyword().get_keyword(result['rsp'], msg_key) in error_msg or GetKeyword().get_keyword(result['rsp'],
                                                                                                         code_key) in error_code:
                payload = kwargs
                child_headers = payload.get('headers')
                child_headers.pop(_get_config()['tokenConf']['token_name'])
                payload['headers'] = child_headers
                return SendMethod().send_method(method, url, **kwargs)
        except json.decoder.JSONDecodeError:
            result['rsp'] = response.text
        return result
