import json


def get_data(filename):
    with open(filename) as file:
        return json.load(file)


def add_data(data: str, path: str):
    with open(path, 'w+') as write_file:
        return json.dump(data, write_file, indent=4)
