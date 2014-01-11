import config

from flask import (request, render_template, session, Blueprint, jsonify, g)
from models import User
from util import *

# The authentication API controls login, logout, and accessing of the session
# state from the client.
authenticate_api = Blueprint('authenticate_api', __name__)

@authenticate_api.route('/login', methods=['POST'])
def login():

    # Get the specified email and password, if they were sent.
    if 'email' not in request.json or 'password' not in request.json:
        return bad_request

    email = request.json['email']
    password = request.json['password']

    # Find out if there is a user with the requested email.
    user = User.query.filter_by(email=email).first()
    if not user:
        return not_authorized

    # There is, so compare credentials.
    hashed_password = password_hash(password, user.salt, config.hash_key)
    if user.password != hashed_password:
        return not_authorized
    else:
        session['user_id'] = user.id
        return jsonify(name=user.name,
                      email=user.email,
                      id=user.id)

@authenticate_api.route('/logout', methods=['POST'])
def logout():
    # Remove the current user from the session.
    if 'user_id' in session:
        session.pop('user_id', None)
        return empty_response
    else:
        return not_authorized

@authenticate_api.route('/user')
def user():
    # Get information about the current user.
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).first()
        return jsonify(name=user.name,
                      email=user.email,
                      id=user.id)
    else:
        return not_authorized