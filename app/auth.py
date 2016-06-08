
from flask import session, redirect, request, render_template
from app import app
from app.models import *

def getUserFromDb(username,password):
    userQuery = Users.query.filter_by(username=username)

    if userQuery.count()==0:
        return "No such user"
    else:
        usr =  userQuery.first()
        if usr.passwordHash==password:
            return usr
        else:
            return "Login failed"

@app.route("/auth/login",methods=["GET","POST"])
def login():
    form = request.form
    if request.method=="POST":
        username = form["username"]
        password = form["password"]
        
        dbUser = getUserFromDb(username,password)

        if type(dbUser) is str:
            return "MSG : BAD LOG IN"

        session['userName']=username
        session['userId']=dbUser.id
        
        return redirect("/users/"+username)
    else:
        return render_template("login.html")

@app.route("/auth/register",methods=["GET","POST"])
def register(username=None):
    form = request.form
    
    #TODO:
    #Make sure unique constraint is satisfied before trying to add to db
    
    if request.method=="POST":
        username = form["username"]
        password = form["password"]
        email = form["email"]
        
        user = Users(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        
        session['userName'] = username
        session['userId'] = user.id
        
        return redirect("/users/"+username)
    else:
        return render_template("register.html")

@app.route("/auth/logout")
def logout():
    session.pop('userName', None)
    session.pop('userId', None)
    session.clear()
    return redirect("/")
