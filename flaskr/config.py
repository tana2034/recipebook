import os


class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class ProductionConfig:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
