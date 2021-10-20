import os

from flask import Flask

from . import main
from . import auth
from . import dashboard

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  app.secret_key=""
  app.register_blueprint(main.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(dashboard.bp)
  return app