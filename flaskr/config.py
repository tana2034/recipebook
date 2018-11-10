import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    SECRET_KEY='dev'

    SQLALCHEMY_TRACK_MODIFICATIONS=True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/recipebook'.format(**{
        'user': os.getenv('POSTGRES_USER', 'postgres'),
        'password': os.getenv('POSTGRES_PASSWORD', 'pass1234'),
        'host': os.getenv('DB_HOST', 'localhost'),
    })

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ECHO = False

