from flask import Flask
app = Flask(__name__)

from notes import views
from notes import schema

