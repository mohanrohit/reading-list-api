import sys
print(sys.path)

import pytest

from app import db
from app.models import User

@pytest.fixture(scope="module")
def new_user():
    pass
    # user = User(first_name="Albert", last_name="Einstein", email="frizzy@me.com")
    # user.save()

    # return user

@pytest.fixture(scope="module")
def init_app():
    app = create_app("testing")

    test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()

@pytest.fixture(scope="module")
def init_db():
    db.create_all()

    db.yield()

    db.drop_all()
