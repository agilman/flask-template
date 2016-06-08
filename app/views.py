from flask import session, render_template
from app import app
from app.models import * 

def getUser(userName):
    query = Users.query.filter_by(username=userName)
   
    if query.count()>0:
        return query.first()

    return "No such user"

@app.route('/SPA')
def spa():
    return render_template('SPA.html')

@app.route('/SPA_editor')
def spa_editor():
    return render_template('SPA_editor.html')

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
    pageOwner = getUser(userName)

    if type(pageOwner) is str:
        return render_template("listViewer.html",msg="Invalid User")

    else:
        userId = pageOwner.id
        userDbName = pageOwner.username
        loginName = None

        if 'userName' in session.keys():
            loginName = session['userName']
            loginId = session['userId']
            if loginId==userId: #If user is looking at his own page... load editor mode
                return render_template("SPA_editor.html", userId=userId)
                
        return render_template("listViewer.html",userName=userDbName, userId=userId, loginName=loginName)

    
