from sensor_api import db

# Drop the databse and all tables
db.reflect()
db.drop_all()
