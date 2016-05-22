
from flask import session, redirect, request, render_template
from app import app
from app.models import db , User

@app.route("/auth/login",methods=["GET","POST"])
def login():
    form = request.form
    if request.method=="POST":
        username = form["username"]
        password = form["password"]

        #Make sure input is valid
        #store userId in session.

        session['username']=username
        
        return redirect("/users/"+username)
    else:
        return render_template("login.html")

@app.route("/auth/register",methods=["GET","POST"])
def register(username=None):
    form = request.form
    
    if request.method=="POST":
        username = form["username"]
        password = form["password"]
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        session['username'] = username
        session['userId'] = user.id
        
        return redirect("/users/"+username)
    else:
        return render_template("register.html")


@app.route("/auth/logout")
def logout():
    session.pop('username', None)
    session.pop('userId', None)
    return redirect("/")
