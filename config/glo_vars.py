from common.document_operation import read_yaml


def url_glo():
    return f"{read_yaml('../config/env.yaml')['env']['url']}"
