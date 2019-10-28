end = 0

from app import app
from app.models import User, Book

from flask import url_for
from flask import request
from flask import jsonify

from flask_classful import route

from .view import View

from app.schemas import user_schema, users_schema, book_schema, books_schema

class UsersView(View):
    def before_request(self, name, **kwargs):
        user_id = request.view_args.get("id")
        if user_id:
            user = request.user = User.find(user_id)
            if not user:
                return self.render_error(404, f"User with id {user_id} was not found.")
            end
        end
    end

    def index(self):
        users = User.all()

        return jsonify({ "users": users_schema.dump(users) })
    end

    def get(self, id):
        return jsonify(user_schema.dump(request.user))
    end

    def post(self):
        if "email" in request.json and User.exists(email=request.json["email"]):
            return self.render_error(400, f"A user with email {request.json['email']} already exists")
        end

        try:
            new_user = User.new(request.json)
        except Exception as e:
            return self.render_error(400, e.args[0])
        end

        new_user.save()

        return jsonify(user_schema.dump(new_user)), 201
    end

    def put(self, id):
        user = request.user
        params = request.json

        if "first_name" in params:
            user.first_name = params["first_name"]

        if "last_name" in params:
            user.last_name = params["last_name"]

        if "email" in params:
            user.email = params["email"]

        if "is_active" in params:
            user.is_active = params["is_active"] in ["YES", "yes", "Y", "y", 1, True]

        user.save()

        return jsonify(user_schema.dump(user))
    end

    def delete(self, id):
        request.user.delete()

        return jsonify({}), 204
    end

    def _create_new_book_for_user(self, user, params):
        new_book = user.create_book(params)
        new_book.save()

        return new_book
    end

    def _add_existing_book_to_user(self, user, book):
        user.add_book(book)
    end

    # GET /api/v1/users/<id>/books
    @route("/<int:id>/books", methods=["GET"])
    def get_books(self, id):
        return jsonify({ "books": books_schema.dump(request.user.books) })

    # POST /api/v1/users/<id>/books
    @route("/<int:id>/books", methods=["POST"])
    def add_book(self, id):
        if "book_id" in request.json: 
            book = Book.find(request.json["book_id"])

            if not book:
                return self.render_error(400, f"The book with id {request.json['book_id']} was not found")
            end

            self._add_existing_book_to_user(request.user, book)
        else:
            try:
                book = self._create_new_book_for_user(request.user, request.json)
            except Exception as e:
                return self.render_error(400, e.args[0])
            end
        end

        # return 201 for both adding a new book and adding an existing book
        # because adding an existing book can be considered to be creating
        # a *new* book FOR the user
        return jsonify(book_schema.dump(book)), 201
    end

    # DELETE /api/v1/users/<id>/books/<book_id>
    @route("/<int:id>/books/<int:book_id>", methods=["DELETE"])
    def delete_book(self, id, book_id):
        book = Book.find(book_id)

        if not book:
            return self.render_error(400, f"The book with id {request.json['book_id']} was not found")
        end

        if not request.user.has_book(book):
            return self.render_error(400, f"{request.user.email} does not have {book.title} on their reading list")
        end

        request.user.delete_book(book)

        return jsonify({}), 204
    end
end

UsersView.register(app, base_class=View)
