from flask import Flask, session

from app import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.sqlalchemy_database_uri
app.secret_key = config.app_secret_key

from app import api
from app import views
from app import schema
from app import auth

