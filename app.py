from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'kdkfkfdg8ioro#'
api = Api(app)

jwt = JWT(app, authenticate, identity)
items = []

class Item(Resource):
   
    def get(self, name):
        item = filter(lambda x: x['name'] == name, items)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if filter(lambda x: x['name'] == name, items):
            return{'message': "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price':data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')

app.run(port=5000, debug=True)