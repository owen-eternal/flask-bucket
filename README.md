# flask-bucket

An extension that uses the flasks command line interface to build a module in your project directory. 

# installation

Run the following to install:
1. Python pip install flask-bucket

# Usage

Import package:
1. from flask_bucket import FlaskBucket 

Initialize package: 
app = Flask(__name__)
FlaskBucket(app)

Run command to create a module:
flask make_module <module_name>