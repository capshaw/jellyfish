from flask import Flask

from configuration import *
from secret_key import SECRET_KEY

from static import static_api
from notes import notes_api

#
# This is the controller for the overall flask application. It sets up the
# proper blueprints for routing the public APIs.
#

# Create a flask application
app = Flask(__name__)
app.config.from_object(__name__)

# Register blueprints for the system APIs
app.register_blueprint(static_api)
app.register_blueprint(notes_api)

# Start the application on running of this file.
if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)