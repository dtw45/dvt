from senseapi import app
from senseapi.views import AccelerometerListView

app.add_url_rule('/accelerometer/', view_func=AccelerometerListView.as_view('accelerometer'))
