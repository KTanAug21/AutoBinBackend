from flask import request, jsonify
from flask_restful import abort
from functools import wraps
import app
import jwt

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print( ' wrapper')
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        else: # throw error if no token provided
            abort( 401, message={'error':'A valid token is missing!'})
        try:
            data = jwt.decode( token, app.config['SECRET_KEY'])
        except:
            abort( 403, message={'error':'Invalid token!'})
        return func( *args, **kwargs )
    return wrapper