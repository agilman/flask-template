from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    passwordHash = db.Column(db.String(128))
    
    toDoLists = db.relationship('ToDoList') 

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class ToDoList(db.Model):
    __tablename__ = 'toDoList'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('user.id'))
    private = db.Column(db.Boolean)
    date = db.Column(db.Date)
    
    items = db.relationship('ToDoItem')
    

class ToDoItem(db.Model):
    __tablename__ = 'toDoItem'
    id = db.Column(db.Integer, primary_key=True)
    toDoList = db.Column(db.Integer,db.ForeignKey('toDoList.id'))
    task = db.Column(db.String(128))
    completed = db.Column(db.Boolean)

