from flask import Flask, request
from flask_restful import Resource, Api 
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
# Authentication
app.secret_key = 'charlie'
# Api from flask restful
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # # Ugly Method
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return {'item': None}, 404
        # Lambda Method
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    def post(self, name):
        # Check name item is unique
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # Get Price from json body
        data = request.get_json(force=True) # force=True (content-type application/json) or silent=True
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        # Set var like global
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)
