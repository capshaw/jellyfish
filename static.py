from flask import (request, render_template, session, Blueprint, jsonify, g)
from util import is_session_current

static_api = Blueprint('static_api', __name__)

@static_api.route('/')
def anon_app():
    return render_template('app.html')