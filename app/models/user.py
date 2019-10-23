from .model import Model, db

class User(Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True, index=True)
    is_active = db.Column(db.Boolean(), default=False, nullable=False)
    books = db.relationship("Book", secondary="user_books", lazy="dynamic")

    def __repr__(self):
        return f"User {self.first_name} {self.last_name}, {self.email}"
