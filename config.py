import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(__file__)
DOTENV_PATH = os.path.join(BASE_DIR, '.env')  # Path to .env file
load_dotenv(DOTENV_PATH)


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/events_db'.format(
        os.getenv('USER'),
        os.getenv('PASSWORD'),
        os.getenv('HOST')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
