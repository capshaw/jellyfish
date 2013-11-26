from flask import (redirect, session, Blueprint, render_template)

from configuration import *

#
# Host the static root application.
#

static_api = Blueprint('static_api', __name__)

@static_api.route("/")
def index():
    ''' Renders the sign in form if the user isn't logged in. '''
    return render_template('default.html', data=data)