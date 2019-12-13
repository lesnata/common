import os


class Config:
    SECRET_KEY = "secret_key_op"


class TestConfig:
    SECRET_KEY = "secret_key_test"


class ProdConfig:
    SECRET_KEY = "secret_key_prod"


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProdConfig
    else:
        return Config
