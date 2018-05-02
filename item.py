from flask_jwt import JWT, jwt_required
from flask_restful import Resource



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    #Require an authorization token for it to be executed.
    @jwt_required()
    def get(self, name):
        global items
        #Next returns the first item found by the list function
        #filter function will only give a filter object hence we use next to return the object
        item = next(filter(lambda x: x['name'] == name, items), None)
        #for item in items:
           #if item['name'] == name:
        return {'item': item}, 200 if item else 404

    def post(self, name):
        global items
        if next(filter(lambda x: x['name'] == name, items), None):
            return{'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price':data['price']}
    
        
        #item = {'name':name, 'price':'2333'}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self,name):

        data = Item.parser.parse_args()

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
