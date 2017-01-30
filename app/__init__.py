# -----------------------------------------------------#
# Imports
# -----------------------------------------------------#

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import load_app_config

# -----------------------------------------------------#
# App Config.
# -----------------------------------------------------#

app = Flask(__name__)
Bootstrap(app)
app.config.update(load_app_config())
#db = SQLAlchemy(app)


from app import route #models, route  # NoQA
