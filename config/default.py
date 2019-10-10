import os

from dotenv import load_dotenv
load_dotenv(verbose=True)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

MIGRATIONS_PATH = f"{os.getcwd()}/db/migrations"

DEBUG = True
DEVELOPMENT = True
TESTING = False
