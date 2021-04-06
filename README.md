# Flask-Resting

A simple REST API module for Flask.

## Setup

To install, run:

```shell
pip install flask-resting
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

## LICENCE
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
