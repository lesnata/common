import json
from os import getcwd
from flask import request


def get_data(filename):
    with open(filename) as some_file:
        return json.load(some_file)


def add_data(data: str, path: str):
    with open(path, 'w+') as write_file:
        return json.dump(data, write_file, indent=4)


def upload_image():
    if request.files['image']:
        img_file = request.files['image']
        img_file.save(f'{getcwd()}/blueprint/products/static_p/{img_file.filename}')
        return img_file.filename
    return 'no-photo.png'
