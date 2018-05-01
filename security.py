from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1,'bob','asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authentication(username,password):
    #Get the username using the get method instead of iterating through the list
    #By using the get method we can set the default value to be None 
    user = username_mapping.get(username, None)
    #By using safe_str_cmp we are able to compare strings for safely
    if user and safe_str_cmp(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)