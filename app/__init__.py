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

# TODO: Use for automated test
# u1 = models.User(first_name="Albert", last_name="Einstein", email="frizzy@me.com")
# u2 = models.User(first_name="Enrico", last_name="Fermi", email="fermi@me.com")
# u3 = models.User(first_name="Paul", last_name="Dirac", email="delta@me.com")
# u4 = models.User(first_name="Werner", last_name="Heisenberg", email="thisorthat@me.com")

# b1 = models.Book(title="Harry Potter 1")
# b2 = models.Book(title="Harry Potter 2")

# u1.books.append(b1)
# u2.books.append(b1)
# b2.owners.append(u3)
# b2.owners.append(u1)
# b2.owners.append(u4)
# for i in [u1, u2, u3, u4, b1, b2]:
#     i.save()
