from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from arm.config.config import cfg

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
