from flask import Flask
from flask_resting import FlaskResting, Resource

app = Flask(__name__)
flask_resting = FlaskResting(app)

class Testing(Resource):
    def get(self):
        return "Hello!"

flask_resting.add_resource(Testing, '/')

if __name__ == '__main__':
    app.run(debug=True)