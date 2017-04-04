from flask import Flask, jsonify, request
from flask.views import MethodView
from senseapi import app, db
from senseapi.schemas import AccelerometerSchema

class AccelerometerListView(MethodView):

    schema = AccelerometerSchema()

    def get(self):
        #TODO: return accelerometer data
        return ""

    def post(self):

        # Deserialize the data and queue to be commited
        for data in request.json:
            instance = self.schema.make_instance(data)
            db.session.add(instance)

        db.session.commit()

        return "200 OK"