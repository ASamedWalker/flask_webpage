import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret!"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f'sqlite:///{os.path.join(basedir, "data.sqlite")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from flask_webpage import routes
