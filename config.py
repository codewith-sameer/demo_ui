import yaml

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)


class Config:
    SQLALCHEMY_DATABASE_URI = config["database"]["uri"]
    SECRET_KEY = config["secret_key"]
