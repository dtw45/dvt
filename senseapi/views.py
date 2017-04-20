from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_api import status
from senseapi import db
from senseapi.models import Accelerometer
from senseapi.schemas import AccelerometerSchema

class AccelerometerListView(MethodView):

    schema = AccelerometerSchema()

    def get(self):

        data = Accelerometer.query.all()

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
