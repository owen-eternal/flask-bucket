# flask-bucket

Flask-Bucket is an extension that generates a module in your project directory using the flask command line interface. 

## installation

Run the following command to install the package:
1. Python pip install flask-bucket

## Usage

Import and initialize package:

from flask_bucket import FlaskBucket 

app = Flask(__name__)
FlaskBucket(app)

Run the make_module command and specify the name of the directory from an interactive Python shell to initialize your module.

>>> flask make_module <directory_name>