end = 0

import os

from datetime import datetime, timedelta

from app.models import User

from flask import url_for
from flask import request
from flask import jsonify

from flask_classful import route

from .view import View

from app.schemas import login_schema

import jwt

class AuthView(View):
    @route("/register", methods=["POST"]) # can't have a method named register()
    # because that's already a method on FlaskView
    def register_user(self):
        if "email" in request.json and User.exists(email=request.json["email"]):
            return self.render_error(400, f"A user with email {request.json['email']} already exists")
        end

        try:
            new_user = User.new(request.json)
        except Exception as e:
            return self.render_error(400, e.args[0])
        end

        new_user.save()

        return jsonify({ "email": new_user.email, "verification_code": 197402, "is_active": new_user.is_active }), 201
    end

    @route("/login", methods=["POST"])
    def login_user(self):
        try:
            login_params = login_schema.load(request.json)
        except Exception as e:
            return self.render_error(400, e.args[0])
        end

        user = User.authenticate(**login_params)

        if not user:
            return self.render_error(400, f"Email or password is incorrect")
        end

        token_dict = {
            "sub": user.email,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }

        token = jwt.encode(token_dict, os.environ.get("JWT_SECRET"), algorithm="HS256")

        return jsonify({ "token": token.decode("UTF-8") })
    end
end
