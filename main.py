import config

from flask import Flask

from authenticate import authenticate_api
from static import static_api
from entries import entries_api
from feed import feed_api

# Create a flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = config.secret_key

# Register blueprints for the system APIs
app.register_blueprint(static_api)
app.register_blueprint(authenticate_api)
app.register_blueprint(entries_api)
app.register_blueprint(feed_api)

# Start the application on running of this file.
if __name__ == "__main__":

    # Note: the parameter "host='0.0.0.0'" allows one to view flask on the
    # local network at the host's public IP address.
    app.run(host='0.0.0.0', debug=True)