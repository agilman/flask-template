from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from collections import OrderedDict
import datetime
from app import app

db = SQLAlchemy(app)

class CommonFuncs(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            attr = getattr(self,key)
            
            #check for non-serializable types
            if type(attr) is datetime.date:
                result[key] = attr.isoformat()
            else:
                result[key] = attr 
        return result


class Users(db.Model,CommonFuncs):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    passwordHash = db.Column(db.String(128))
    
    toDoLists = db.relationship('ToDoLists') 

    def __init__(self, username,password,email):
        self.username = username
        self.email = email
        self.passwordHash = password

    def __repr__(self):
        return '<User %r>' % self.username


class ToDoLists(db.Model,CommonFuncs):
    __tablename__ = 'toDoLists'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('users.id'))
    name = db.Column(db.String(64))
    private = db.Column(db.Boolean)
    date = db.Column(db.Date)
    
    items = db.relationship('ToDoItems', cascade="save-update, merge, delete")

class ToDoItems(db.Model,CommonFuncs):
    __tablename__ = 'toDoItems'
    id = db.Column(db.Integer, primary_key=True)
    listId = db.Column(db.Integer,db.ForeignKey('toDoLists.id'))
    task = db.Column(db.String(128))
    completed = db.Column(db.Boolean)

