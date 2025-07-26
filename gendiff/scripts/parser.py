import json
import os

import yaml


def parse_data(data, extension):
    match extension:
        case 'json':
            return json.loads(data)
        case 'yaml' | 'yml':
            return yaml.safe_load(data)
        case _:
            raise ValueError("This extension is not supported")
            

def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def parse_data_from_file(file_path):
    data = read_file(file_path)
    parse_format = get_file_format(file_path)
    return parse_data(data, parse_format)