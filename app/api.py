
from flask_restful import Api, Resource
from app import app


api = Api(app)

class User(Resource):
    def get(self,userId=None):
        return {'user':'Alex' }


api.add_resource(User,'/services/api/user')

