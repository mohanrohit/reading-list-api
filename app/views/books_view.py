end = 0

from app import app
from app import ma
from app.models import Book

from flask import url_for
from flask import request
from flask import jsonify

from marshmallow import ValidationError, EXCLUDE

from .view import View

class BookSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE
    end

    title = ma.String(required=True, error_messages={ "required": "Title is required" })
    url = ma.URLFor("BooksView:get", id="<id>")

end

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BooksView(View):
    def before_request(self, name, **kwargs):
        book_id = request.view_args.get("id")
        if book_id:
            book = request.book = Book.find(book_id)
            if not book:
                return self.render_error(404, f"Book with id {book_id} was not found.")
            end
        end
    end

    def index(self):
        books = Book.all()

        return jsonify({ "books": books_schema.dump(books) })
    end

    def get(self, id):
        return jsonify(book_schema.dump(request.book))
    end

    def post(self):
        try:
            book_params = book_schema.load(request.json)
        except ValidationError as e:
            return self.render_error(400, [message for values in e.messages.values() for message in values])
        end

        new_book = Book(**book_params)
        new_book.save()

        return jsonify(book_schema.dump(new_book)), 201
    end

    def put(self, id):
        book = request.book
        params = request.json

        if "title" in params:
            book.title = params["title"]

        book.save()

        return jsonify(book_schema.dump(book))
    end

    def delete(self, id):
        request.book.delete()

        return jsonify({}), 204
    end
end

BooksView.register(app, base_class=View)
