from app import ma

from marshmallow import ValidationError, EXCLUDE

class UserSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE

    first_name = ma.String(required=True, error_messages={ "required": "First name is required" })
    last_name = ma.String(required=True, error_messages={ "required": "Last name is required" })
    email = ma.String(required=True, error_messages={ "required": "Email is required" })
    url = ma.URLFor("UsersView:get", id="<id>")
    is_active = ma.Boolean()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
