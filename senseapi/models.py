from senseapi import db
from sqlalchemy import Column, Integer, DateTime, Float

class Accelerometer(db.Model):

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)
