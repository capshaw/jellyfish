import config
import random

from functools import wraps
from flask import g, request, redirect, url_for, session
from werkzeug.wrappers import BaseResponse as Response

from hashlib import sha512
from math import ceil

# The default number of entries to page when paginating.
ENTRIES_PER_PAGE = 10

# Various reusable responses.
empty_response = Response('')
not_found = Response('Not Found', status=404)
not_authorized = Response('Not Authorized', status=401)
bad_request = Response('Bad Request', status=400)
im_a_teapot = Response('I\'m a Teapot', status=418)

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

def paginate_helper(query, page, entries_per_page=ENTRIES_PER_PAGE):
    # Given a query and page, return a list of the elements on that page.
    offset = (page - 1) * entries_per_page
    total_pages = ceil(query.count() / (1.0 * entries_per_page))
    entries = query.limit(entries_per_page).offset(offset)
    return (entries, total_pages)

# TODO: make this redirect to the page that the user originally requested
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function