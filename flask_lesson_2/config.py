import os


class Config(object):
    SECRET_KEY = os.environ.get('OY_VEY_SECRET_KEY') or 'you-will-never-guess-oy-vey-2'
    DEBUG = True

