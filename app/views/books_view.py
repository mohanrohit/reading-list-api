end = 0

import os

from functools import wraps

from app.models import Book, User

from flask import url_for, redirect
from flask import request
from flask import jsonify

import jwt

from .view import View

from app.schemas import book_schema, books_schema
from app.schemas import user_books_schema

# decorator to get a user from the request
#@staticmethod
def user(function):
    @wraps(function)
    def _get_user(*args, **kwargs):
        request.user = None

        if not "Authorization" in request.headers:
            return function(*args, **kwargs)
        end

        auth_headers = request.headers.get("Authorization").split()

        if len(auth_headers) != 2:
            return function(*args, **kwargs)
        end

        auth_token = jwt.decode(auth_headers[1], os.getenv("JWT_SECRET"), algorithms=["HS256"])

        request.user = User.find_one(email=auth_token["sub"])

        return function(*args, **kwargs)
    end

    return _get_user
end

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

    # return a list of all books or books belonging to a user
    # depending on the param owner=none or owner=me or
    # owner=<user-id>. for owner=<user-id>, either the logged
    # in user must be admin or the <user-id> must be the same
    # as the logged in user.
    @user
    def index(self):
        if not request.user:
            books = Book.all()

            return jsonify({ "books": books_schema.dump(books) })
        end

        owner = request.args.get("owner")

        if not owner or owner == "me" or owner == str(request.user.id):
            books = request.user.get_books()

            return jsonify({ "books": user_books_schema.dump(books) })
        end

        # owner is a user-id. show books only if the logged in user
        # is admin
        if not request.user.is_admin():
            return self.render_error(403, "You are not authorized to see another user's books")
        end

        other_user = User.find(owner)

        if not other_user:
            return self.render_error(400, f"No user with id {owner} was found.")
        end

        books = other_user.get_books()

        return jsonify({ "books": user_books_schema.dump(books) })
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
