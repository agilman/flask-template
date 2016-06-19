
from flask_restful import Api, Resource
from flask import jsonify, request
from app import app
from sqlalchemy import update
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
    def get(self,userId):
        #TODO input validation.. check if key exists?
        #userId = request.args['userId']

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

class Lists(Resource):
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

    def delete(self,listId):
        #TODO input validation.. check if key exists?
        #listId = request.args['listId']
        
        query = ToDoLists.query.filter_by(id = listId)
        li = query.first()
        
        db.session.delete(li)
        db.session.commit()

        return jsonify(deleted=li._asdict())

class ListItems(Resource):
    def post(self):
        jsonDict = request.get_json()
        
        #TODO check if keys were passed
        listId = jsonDict['listId']
        task = jsonDict['task']
        newItem = ToDoItems(listId=listId,task=task)
        
        #todo : try except
        db.session.add(newItem)
        db.session.commit()
        
        return jsonify(newItem=newItem._asdict())

    def put(self):
        jsonDict = request.get_json()        
        itemId= jsonDict['id']
        completed = jsonDict['completed']

        item = ToDoItems.query.filter_by(id=itemId).first()
        
        #to do... update all attributes
        item.completed = completed

        db.session.commit()
     
        return {'itemId':itemId,'status':'ok'}

    def delete(self,itemId):
        query = ToDoItems.query.filter_by(id=itemId)
        item = query.first()
        
        db.session.delete(item)
        db.session.commit()
        
        return jsonify(deleted = item._asdict())
        
api.add_resource(UserLists,'/services/api/userLists/<int:userId>')
api.add_resource(Lists,'/services/api/lists/<int:listId>','/services/api/lists')
api.add_resource(ListItems,'/services/api/listItems/<int:itemId>','/services/api/listItems')

