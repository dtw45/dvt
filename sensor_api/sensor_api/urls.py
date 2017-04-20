from sensor_api import app
from sensor_api.views import AccelerometerListView

app.add_url_rule('/accelerometer/', view_func=AccelerometerListView.as_view('accelerometer'))
