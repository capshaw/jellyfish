import config

from flask import Flask

from authenticate import authenticate_api
from static import static_api
from entries import entries_api

# Create a flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = config.secret_key

# Register blueprints for the system APIs
app.register_blueprint(static_api)
app.register_blueprint(authenticate_api)
app.register_blueprint(entries_api)

# Start the application on running of this file.
if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)