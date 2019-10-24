from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("config.default")
app.config.from_envvar("CONFIG")

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db, directory=app.config["MIGRATIONS_PATH"])

CORS(app)

from app import models, views
print("imported models and views")
