from werkzeug.security import safe_str_cmp
from user import User

# # Ugly Method Without Class
# users = [
#     {
#         'id': 1,
#         'username': 'charlie',
#         'password': 'asdasd'
#     }
# ]
# username_mapping = { 'charlie': {
#     'id': 1,
#     'username': 'charlie',
#     'password': 'asdasd' 
# }}
# userid_mapping = { 1: {
#     'id': 1,
#     'username': 'charlie',
#     'password': 'asdasd'  
# }}

# Pro method

users = [
    User(1, 'charlie', 'asdasd')
]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    # Could be a problem with unicode
    # if user and user.password == password:
    if user and safe_str_cmp(user.password, password): # More safe
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)