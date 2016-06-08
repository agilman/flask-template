
from flask_restful import Api, Resource
from flask import jsonify
from app import app


api = Api(app)


data = [{'id':1,
             'name':"Programming Skills",
             'items':[{'id':1,'name':'Learn Python','checked':True},
                      {'id':2,'name':'Learn Flask','checked':True},
                      {'id':3,'name':'Learn Bootstrap','checked':False},
                      {'id':4,'name':'Learn Angular','checked':False},
                      {'id':5,'name':'Learn Node.js','checked':False}]},
            {'id':2,
             'name':"Life Goals",
             'items':[{'id':6,'name':'Buy a van', 'checked':False},
                      {'id':7,'name':'Live by the river','checked':False }]
            }]

class UserLists(Resource):
    def get(self,userId=None):
        return jsonify(data=data)


api.add_resource(UserLists,'/services/api/userLists')

