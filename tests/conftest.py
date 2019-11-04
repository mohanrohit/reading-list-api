end = 0

import os
import sys

sys.path.append(os.getcwd())

import pytest

from app import create_app
from app import db
from app.models import User, Book

from tests.api import API

@pytest.fixture(scope="session")
def test_client():
    app = create_app("testing")

    test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()
end

@pytest.fixture(scope="session")
def init_db():
    db.create_all()

    user1 = User(first_name="Albert", last_name="Einstein", email="frizzy@me.com")
    user2 = User(first_name="Enrico", last_name="Fermi", email="fermi@me.com")
    user3 = User(first_name="Paul", last_name="Dirac", email="delta@me.com")
    user4 = User(first_name="Werner", last_name="Heisenberg", email="thisorthat@me.com")

    book1 = Book(title="Harry Potter and the Sorcerer's Stone")
    book2 = Book(title="Harry Potter and the Chamber of Secret")
    book3 = Book(title="Harry Potter and the Prisoner of Azkaban")

    user1.books.append(book1)
    user2.books.append(book1)
    book2.owners.append(user3)
    book2.owners.append(user1)
    book2.owners.append(user4)

    for ob in [user1, user2, user3, user4, book1, book2, book3]:
        ob.save()
    end

    yield db

    db.drop_all()
end

@pytest.fixture(scope="session")
def api(test_client, init_db):
    return API(test_client)
end
