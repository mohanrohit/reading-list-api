import sys

from end_statement import end

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

from models import *

# import all controllers modules, and for each controller module,
# register the app for the controller class in that module
from controllers import *

controller_modules = [sys.modules[module_name] for module_name in sys.modules if module_name.endswith("_controller")]

controller_classes = [getattr(module, attribute) for module in controller_modules for attribute in dir(module) if attribute.endswith("Controller")]
for controller_class in controller_classes:
  controller_class.register(app, route_base="/", trailing_slash=False)
end
