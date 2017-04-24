from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_api import status

from sensor_api import db

from sensor_api.models import Accelerometer
from sensor_api.models import Gyroscope
from sensor_api.models import Magnetometer
from sensor_api.models import Emg

from sensor_api.schemas import AccelerometerSchema
from sensor_api.schemas import GyroscopeSchema
from sensor_api.schemas import MagnetometerSchema
from sensor_api.schemas import EmgSchema


class BaseListView(MethodView):

    model = None
    schema = None

    def get(self):

        data = self.model.query.all()

        response = self.schema.dump(data, many=True).data

        return jsonify(response)

    def post(self):

        # Deserialize and validtate the data
        instances, errors = self.schema.load(request.json, many=True)

        if errors:
            return jsonify({'errors': errors}), status.HTTP_400_BAD_REQUEST

        # Save to the database
        db.session.add_all(instances)
        db.session.commit()

        # Don't deserialize objects. Only the microprocessor should
        # be posting data and it does not need the new objects.
        return jsonify({"message": "objects created"}), status.HTTP_201_CREATED


class AccelerometerListView(BaseListView):

    model = Accelerometer
    schema = AccelerometerSchema()


class GyroscopeListView(BaseListView):

    model = Gyroscope
    schema = GyroscopeSchema()


class MagnetometerListView(BaseListView):

    model = Magnetometer
    schema = MagnetometerSchema()


class EmgListView(BaseListView):

    model = Emg
    schema = EmgSchema()
