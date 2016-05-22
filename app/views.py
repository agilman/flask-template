from flask import session, render_template
from app import app
from app.models import * 

def getUserId(userName):
    query = User.query.filter_by(username=userName)
   
    if query.count()>0:
        return query.first().id

    return 0

@app.route('/')
def index():
    if 'userName' in session.keys():
        userName = session['userName']
        userId = session['userId']
        return render_template("landingSession.html", userName=userName,userId=userId)
    else:
        return render_template("landing.html")

@app.route('/users/<userName>')
def users(userName):
    userId = getUserId(userName)

    if userId==0:
        return "NO SUCH USER"

    else:
        if 'userId' in session.keys():
            if session['userId']==userId:
                return "editor template"
                
        return "viewer template"

    
