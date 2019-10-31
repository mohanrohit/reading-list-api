end = 0

from flask import url_for

from .schema import Schema, ValidationError

class UserBookSchema(Schema):
    def __init__(self, many=False):
        Schema.__init__(self, many)
    end

    def transform(self, user_book):
        return \
        {
            "title": user_book.book.title,
            "url": url_for("BooksView:get", id=user_book.book.id),
            "is_read": user_book.is_read
        }
    end
end

user_book_schema = UserBookSchema()
user_books_schema = UserBookSchema(many=True)
