from werkzeug.security import safe_str_cmp
from user import User



def authenticate(username,password):
    #Get the username using the get method instead of iterating through the list
    #By using the get method we can set the default value to be None 
    user = User.find_by_username(username)
    #By using safe_str_cmp we are able to compare strings for safely
    if user and safe_str_cmp(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)