from flask import jsonify
from flask import request

from flask_classful import FlaskView

class View(FlaskView):
    route_prefix = "/api/v1"
    trailing_slash = False

    def before_post(self):
        if not request.is_json:
            return self.render_error(406, "JSON payload is required.")

    def render_object(self, object, **options):
        return jsonify(object), options["status"] if options.get("status") else 200

    def render_error(self, status_code, message):
        if isinstance(message, list):
            return jsonify({ "code": status_code, "message": ", ".join(message) }), status_code
        else:
            return jsonify({ "code": status_code, "message": message }), status_code
