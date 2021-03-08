import sys  # noqa: F401
import os  # noqa: F401
import bcrypt  # noqa: F401

from flask import Flask, logging, current_app  # noqa: F401
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from arm.config.config import cfg
from flask.logging import default_handler  # noqa: F401
from getpass import getpass  # noqa: F401
# import omdb

from flask_login import LoginManager

sqlitefile = 'sqlite:///' + cfg['DBFILE']

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = sqlitefile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# We should really gen a key for each system
app.config['SECRET_KEY'] = "Big secret key"
# TODO: the database is defined in the UI-module - that seems just wrong
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# omdb.set_default('apikey', cfg['OMDB_API_KEY'])

# import arm.ui.routes  # noqa: E402,F401
# import models.models  # noqa: E402
# import ui.config  # noqa: E402
# import ui.utils  # noqa: E402,F401
