end = 0

from flask import url_for

from .schema import Schema, ValidationError

class BookSchema(Schema):
    def __init__(self, many=False):
        Schema.__init__(self, many)
    end

    def validate(self, params):
        self.validate_required(params, "title", "The title of the book is required")

        return { "title": params["title"] }
    end

    def transform(self, book):
        return \
        {
            "title": book.title,
            "url": url_for("BooksView:get", id=book.id)
        }
    end
end

book_schema = BookSchema()
books_schema = BookSchema(many=True)
