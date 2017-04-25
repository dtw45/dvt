from sensor_api import app, ma

from sensor_api.models import Accelerometer
from sensor_api.models import Gyroscope
from sensor_api.models import Magnetometer
# from sensor_api.models import Emg


class AccelerometerSchema(ma.ModelSchema):

    class Meta:
        model = Accelerometer


class GyroscopeSchema(ma.ModelSchema):

    class Meta:
        model = Gyroscope


class MagnetometerSchema(ma.ModelSchema):

    class Meta:
        model = Magnetometer


# class EmgSchema(ma.ModelSchema):
#
#     class Meta:
#         model = Emg
