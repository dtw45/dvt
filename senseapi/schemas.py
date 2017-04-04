from senseapi import app, ma
from senseapi.models import Accelerometer
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import field_for

class AccelerometerSchema(ma.ModelSchema):

    class Meta:
        model = Accelerometer
