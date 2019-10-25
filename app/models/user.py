from .model import Model, db

from .book import Book

class User(Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True, index=True)
    is_active = db.Column(db.Boolean(), default=False, nullable=False)
    books = db.relationship("Book", secondary="user_books", lazy="dynamic")

    def create_book(self, book_params):
        try:
            new_book = Book.new(book_params)
        except Exception as e:
            raise

        self.add_book(new_book)

        return new_book

    def add_book(self, book):
        self.books.append(book)

        self.save()

        return book

    def __repr__(self):
        return f"User {self.first_name} {self.last_name}, {self.email}"
