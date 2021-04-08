# Flask-Resting

A simple REST API module for Flask.

## Setup

To install, run:

```shell
pip install git+https://github.com/TechStudent11/Flask-Resting.git
```

or:

```shell
git clone https://github.com/TechStudent11/Flask-Resting
cd Flask-Resting
pip install .
```

## Basic Usage

A basic REST API using this module would look like:

```python
from flask import Flask
from flask_resting import FlaskResting, Resource

app = Flask(__name__)
api = FlaskResting(app)

users = {}

class UserView(Resource):
    def get(self, id):
        return users.get(id)
    
    def post(self, id):
        users[id] = {'id': id}
        return users[id]

api.add_resource(UserView, '/user/<id>')

if __name__ == '__main__':
    app.run(debug=True)
```
