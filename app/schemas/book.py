from app import ma

from marshmallow import EXCLUDE

class BookSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE

    title = ma.String(required=True, error_messages={ "required": "The title of the book is required" })
    url = ma.URLFor("BooksView:get", id="<id>")

book_schema = BookSchema()
books_schema = BookSchema(many=True)
