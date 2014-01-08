from flask import (request, render_template, session, Blueprint, jsonify, g)
from util import is_session_current

static_api = Blueprint('static_api', __name__)

@static_api.route('/')
def anon_app():
    if is_session_current():
        return render_template('mainApp.html')
    else:
        return render_template('anonApp.html')