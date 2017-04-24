from sensor_api import app
from sensor_api.views import AccelerometerListView
from sensor_api.views import GyroscopeListView
from sensor_api.views import MagnetometerListView


app.add_url_rule('/accelerometer/', view_func=AccelerometerListView.as_view('accelerometer'))
app.add_url_rule('/gyroscope/', view_func=GyroscopeListView.as_view('gyroscope'))
app.add_url_rule('/magnetometer/', view_func=MagnetometerListView.as_view('magnetometer'))
