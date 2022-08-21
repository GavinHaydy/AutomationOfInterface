import yaml


def read_yaml(filepath):
    return yaml.load(open(filepath, 'r').read(), yaml.FullLoader)
