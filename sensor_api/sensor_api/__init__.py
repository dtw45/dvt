from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# create the application object
app = Flask(__name__)

# load configuration settings
app.config.from_object('config.BaseConfig')

# create the sqlalchemy object
db = SQLAlchemy(app)
ma = Marshmallow(app)

import urls
