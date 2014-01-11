import config
import random

from functools import wraps
from flask import g, request, redirect, url_for, session
from werkzeug.wrappers import BaseResponse as Response

from hashlib import sha512

# Various reusable responses.
empty_response = Response('', status=201)
not_found = Response('Not Found', status=404)
not_authorized = Response('Not Authorized', status=401)
bad_request = Response('Bad Request', status=400)

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def hash_user_password(user):
    user.password = password_hash(user.password, user.salt, config.hash_key)
    return user

def password_hash(string, salt, secret_key):
    return sha512(salt + string + secret_key + secret_key + salt).hexdigest()

def generate_salt(how_long):
    return ''.join(random.choice(ALPHABET) for i in range(how_long))

def is_session_current():
    # Returns True if there is a current, valid, session. Else, returns False.
    if 'user_id' in session:
        return True
    return False

# TODO: make this redirect to the page that the user originally requested
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function