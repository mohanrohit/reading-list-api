end = 0

from flask import url_for

from .schema import Schema, ValidationError

class LoginSchema(Schema):
    def __init__(self, many=False):
        Schema.__init__(self, many)
    end

    def validate(self, params):
        self.validate_required(params, "email", "Email is required")
        self.validate_required(params, "password", "Password is required")

        return { "email": params["email"], "password": params["password"] }
    end

    def transform(self, params):
        raise Exception("Cannot call transform() for LoginSchema")
    end
end

login_schema = LoginSchema()
