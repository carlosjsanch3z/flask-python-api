from flask import Flask 
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

class Customer(Resource):
    def get(self, name):
        return {'customer': name}

api.add_resource(Customer, '/customer/<string:name>') # http://127.0.0.1:5000/customer/Charlie

app.run(port=5000)
