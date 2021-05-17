# flask-bucket

Flask-Bucket is an extension that uses the flask command line interface to create a module inside your project directory. It comes in handy when operating in a flask application factory configuaration. 

## Installation

Run the following command to install:

```python
>>> Python pip install flask-bucket
```
## Usage

1. Import and initialize the package inside the **create_app** function.
2. Import your module and register your blueprint object.  

```python

from flask_bucket import FlaskBucket 

def create_app():

    app = Flask(__name__)
    FlaskBucket(app)
    
    from .<module_name>.routes import <blueprint_name>
    app.registerblueprint(<blueprint_name>)

    return app
```

Initialize your module by running the **make_module** command from an interactive Python shell and specify the name of the directory. **Note** The package automatically produces a blueprint and a routes layout inside your
**routes.py** file, located inside the module.

```python
>>> flask make_module <directory_name>
```
