end = 0

from .model import Model, db

from .book import Book
from .user_book import UserBook

class User(Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True, index=True)
    is_active = db.Column(db.Boolean(), default=False, nullable=False)
    books = db.relationship("Book", secondary="user_books", lazy="dynamic", backref="owners")

    def has_book(self, book):
        return True if UserBook.find_one(user_id=self.id, book_id=book.id) else False
    end

    def create_book(self, book_params):
        new_book = Book.new(book_params)

        # if you're creating a new book, the is_read attribute
        # will be false (or why would you add it to a reading list?)
        user_book = UserBook(user=self, book=new_book)
        user_book.save()

        return user_book
    end

    def get_book(self, book_id):
        user_book = UserBook.find_one(user_id=self.id, book_id=book_id)

        return user_book
    end

    def add_book(self, book):
        user_book = self.get_book(book.id)

        if not user_book:
            user_book = UserBook(user=self, book=book)
            user_book.save()
        end

        return user_book
    end

    def delete_book(self, book):
        users_book = UserBook.find_one(user_id=self.id, book_id=book.id)
        if users_book:
            users_book.delete()
        end
    end

    def __repr__(self):
        return f"User ({self.first_name} {self.last_name}, {self.email})"
    end
