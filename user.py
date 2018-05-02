import sqlite3
from flask_restful import Resource,reqparse

class User():

    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            #id,username,password
            #set of positional argument
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls,id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        if row:
            #id,username,password
            #set of positional argument
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field is required!"
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field is required!"
    )

    def post(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        data = UserRegister.parser.parse_args()
        query = "INSERT INTO users VALUES (NULL, ? , ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message":"User created successfully"}, 201
