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
    #Require an authorization token for it to be executed.
    @jwt_required()
    def get(self, name):
        #Next returns the first item found by the list function
        #filter function will only give a filter object hence we use next to return the object
        item = next(filter(lambda x: x['name'] == name, items), None)
        #for item in items:
           #if item['name'] == name:
        return {'item': item}, 200 if item else 404

    def post(self, name):
        
        if next(filter(lambda x: x['name'] == name, items), None):
            return{'message': "An item with name '{}' already exists".format(name)}, 400

        
        item = {'name': name, 'price':data['price']}
    
        data = request.get_json()
        #item = {'name':name, 'price':'2333'}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self,name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')

app.run(port=5000, debug=True)