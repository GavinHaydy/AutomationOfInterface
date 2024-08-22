"""
    @Author: Gavin
    @Email: bugpz2779@gmail.com theruffian@163.com
    @Blog: 'https://blog.csdn.net/BUGPZ'
    @StackOverFlow: 'https://stackoverflow.com/users/12850648/theruffian'
    @Github: 'https://github.com/GavinHaydy'
"""
import redis
import yaml


def rds(host: str = 'localhost', port: int = 6379, db: int = 0, password: str = None):
    """

    Args:
        host: redis server ip
        port: redis server port
        db: redis db number
        password: redis password -> str|None

    Returns: redis client

    """
    try:
        if password:
            return redis.StrictRedis(host, port, db, password)
        else:
            return redis.StrictRedis(host=host, port=port, db=db)
    except Exception as e:
        return e
def read_yaml(filepath):
    """

    Args:
        filepath: yaml file path

    Returns: dict

    """
    return yaml.load(open(filepath, 'r').read(), yaml.FullLoader)
