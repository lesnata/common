import json


def get_data(filename):
    with open(filename) as some_file:
        return json.load(some_file)


def add_data(data: str, path: str):
    with open(path, 'w+') as write_file:
        return json.dump(data, write_file, indent=4)

