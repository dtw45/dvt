from senseapi import db

# Drop the databse and all tables
db.reflect()
db.drop_all()
