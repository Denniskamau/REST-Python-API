from flask import Flask, request
from flask_restful import  Api,reqparse
from flask_jwt import JWT
from user import UserRegister
from security import authenticate, identity
from item import Item,ItemList


app = Flask(__name__)
app.secret_key = 'kdkfkfdg8ioro#'
api = Api(app)

jwt = JWT(app, authenticate, identity)



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')
api.add_resource(UserRegister, '/register/')

app.run(port=8000, debug=True)