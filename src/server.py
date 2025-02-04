import os
from flask import Flask
from certification_controller import certification_controller_bp


app = Flask(__name__)
# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT

cf_port = os.getenv("PORT")

app.register_blueprint(certification_controller_bp, url_prefix='/certification')

# Only get method by default
@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
	if cf_port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(cf_port), debug=True)