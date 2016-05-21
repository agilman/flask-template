
from flask import redirect, request
from app import app


@app.route("/auth/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        session['username']=request.form['username']
        return redirect("/")
    else:
        return "LOGIN FORM HERE"
