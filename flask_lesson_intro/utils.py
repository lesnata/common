import json


def get_data():
    with open("data.json") as fileitem:
        return json.load(fileitem)

