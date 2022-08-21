# @Author: the_ruffian
# @email: 13558622779@163.com/bugpz2779@gmail.com

from requests import request
from interface.login import token


class Foo:
    def __getattribute__(self, item):
        attr = object.__getattribute__(self,item)
        if hasattr(attr, '__call__'):
            def new_func(*args, **kwargs):
                print('before calling %s' % attr.__name__)
                if kwargs.get('headers'):
                    result = attr(*args, **kwargs)
                    print('done calling %s' % attr.__name__)
                    return result
                else:
                    headers = {}
                    headers['Authorization'] = token()
                    kwargs.setdefault('headers',headers)
                    return attr(*args,**kwargs)

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
            raise ValueError(f'请求方式"{method}"暂不支持')
        result = dict()

        result['req'] = response.request     # 请求体
        result['res'] = response.json()     # 响应体

        return result
