from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost/multi_step_form"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)
marshmallow = Marshmallow(app)
CORS(app)

from routes.registration.registration_routes import registration_blueprint

app.register_blueprint(registration_blueprint)
