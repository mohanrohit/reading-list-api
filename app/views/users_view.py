end = 0

from app import app
from app.models import User

from flask import url_for
from flask import request
from flask import jsonify

from flask_classful import route

from .view import View

from app.schemas import user_schema, users_schema

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

    @route("/<int:id>/books", methods=["POST"])
    def add_book(self, id):
        user = request.user
        params = request.json
        new_book = user.create_book(request.json)
        return jsonify({ "title": new_book.title })
    end
end

UsersView.register(app, base_class=View)
