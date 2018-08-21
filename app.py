from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
import settings
from flask_cors import CORS

app = Flask(__name__)
# to enable a better debugging locally, use CORS
CORS(app)
app.api = Api(app, title='C1 Test API', description="An example C1 API", validate=True)
# secret key for sessions usage
app.secret_key = 'v5dw72S4VjkXj9ndE39K'
app.config.from_object(settings)
app.db = SQLAlchemy(app)

def get_app():
    global app
    return app
