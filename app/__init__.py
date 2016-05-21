from flask import Flask
from app import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.sqlalchemy_database_uri

from app import views
from app import schema

