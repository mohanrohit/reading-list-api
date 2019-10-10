from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("config.default")
app.config.from_envvar("CONFIG")

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db, directory=app.config["MIGRATIONS_PATH"])

from app import models, views
