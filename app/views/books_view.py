end = 0

from app.models import Book

from flask import url_for
from flask import request
from flask import jsonify

from .view import View

from app.schemas import book_schema, books_schema

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
            new_book = Book.new(request.json)
        except Exception as e:
            return self.render_error(400, e.args[0])
        end

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
