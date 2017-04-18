from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_api import status
from senseapi import app, db
from senseapi.models import Accelerometer
from senseapi.schemas import AccelerometerSchema

class AccelerometerListView(MethodView):

    schema = AccelerometerSchema()

    def get(self):

        data = Accelerometer.query.all()

        response = self.schema.dump(data, many=True).data

        return jsonify(response)

    def post(self):

        # Deserialize the data and queue to be commited
        for d in request.json:
            instance, errors = self.schema.load(d)

            if errors:
                return jsonify({'errors': errors}), 422

            import ipdb; ipdb.set_trace()
            instance.save()
        #     db.session.add(instance)
        #
        # db.session.commit()

        # response = []
        #
        # for data in request.json:
        #     response.append(self.schema.load(data).data)

        return jsonify(instance)
