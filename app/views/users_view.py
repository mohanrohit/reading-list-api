end = 0

from app import app
from app import ma
from app.models import User

from flask import url_for
from flask import request
from flask import jsonify

from marshmallow import ValidationError, EXCLUDE

from .view import View

class UserSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE
    end

    def is_user_active(self, user):
        return "yes" if user.is_active else "no"
    end

    first_name = ma.String(required=True, error_messages={ "required": "First name is required" })
    last_name = ma.String(required=True, error_messages={ "required": "Last name is required" })
    email = ma.String(required=True, error_messages={ "required": "Email is required" })
    url = ma.URLFor("UsersView:get", id="<id>")
    is_active = ma.Method("is_user_active")
end

user_schema = UserSchema()
users_schema = UserSchema(many=True)

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
        try:
            user_params = user_schema.load(request.json)
        except ValidationError as e:
            return self.render_error(400, [message for values in e.messages.values() for message in values])
        end

        if User.exists(email=user_params["email"]):
            return self.render_error(400, f"A user with email {user_params['email']} already exists")
        end

        new_user = User(**user_params)
        new_user.save()

        return jsonify(user_schema.dump(new_user)), 201
    end

    def put(self, id):
        user = request.user
        params = request.json

        if params.get("first_name"):
            user.first_name = params["first_name"]

        if params.get("last_name"):
            user.last_name = params["last_name"]

        if params.get("is_active"):
            user.is_active = params["is_active"] in ["YES", "yes", "Y", "y", 1]

        user.save()

        return jsonify(user_schema.dump(user))
    end

    def delete(self, id):
        request.user.delete()

        return jsonify({}), 204
    end

UsersView.register(app, base_class=View)
