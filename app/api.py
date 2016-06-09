
from flask_restful import Api, Resource
from flask import jsonify, request
from app import app
from app.models import *

api = Api(app)

def addToOrderedDict(oldDict,label,item):
    """Creates a new ordered dictionary, containin old dictionary and a new key-value pair"""

    newDict = []
    for i in oldDict.keys():
        newDict.append((i,oldDict[i] ))
        items=[]

    newDict.append((label,item))
    return OrderedDict(newDict)

class UserLists(Resource):
    def get(self):
        #TODO input validation.. check if key exists?
        userId = request.args['userId']

        listsQuery = ToDoLists.query.filter_by(userId=userId)
        results = []
        for li in listsQuery.all():
            tempLi = li._asdict()
            
            items = []
            for item in li.items:
                items.append(item._asdict())

            newLi = addToOrderedDict(tempLi,'items',items)
            results.append(newLi)

        return jsonify(lists=results)

    def post(self):
        jsonDict = request.get_json()
        
        #TODO check if keys were passed...
        userId= jsonDict['userId']
        name = jsonDict['name']
        newList = ToDoLists(userId=userId,name=name)
        
        #todo : try except
        db.session.add(newList)
        db.session.commit()
        
        return jsonify(newList=newList._asdict())

api.add_resource(UserLists,'/services/api/userLists')

