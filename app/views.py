from app import app
from app.models import * 

def getUserId(userName):
    query = User.query.filter_by(username=userName)
    
    if query.count()>0:
        return query.first().id

    return 0

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/users/<userName>')
def users(userName):
    userId = getUserId(userName)

    if userId==0:
        return "NO SUCH USER"

    else:
        return ("OK< here is the user: %s" %userId)
    
