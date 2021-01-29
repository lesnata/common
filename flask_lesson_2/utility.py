import json
from os import getcwd
from flask import request
from PIL import Image


def get_data(filename):
    with open(filename) as some_file:
        return json.load(some_file)


def add_data(data: str, path: str):
    with open(path, 'w+') as write_file:
        return json.dump(data, write_file, indent=4)


def upload_image_product():
    if request.files['image']:
        img_file = request.files['image']
        img_compressed = Image.open(img_file)
        img_compressed.save(f'{getcwd()}/blueprint/products/static_p/{img_file.filename}')
        return img_file.filename
    return 'no-photo.png'


def upload_image_supermarket():
    if request.files['image']:
        img_file = request.files['image']
        img_compressed = Image.open(img_file)
        img_compressed.save(f'{getcwd()}/blueprint/supermarkets/static_s/{img_file.filename}')
        return img_file.filename
    return 'no-photo.png'

