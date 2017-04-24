from sqlalchemy import Column, Integer, DateTime, Float

from sensor_api import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)


class TriaxialModel(BaseModel):
    __abstract__ = True

    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)


class Accelerometer(TriaxialModel):
    pass


class Gyroscope(TriaxialModel):
    pass


class Magnetometer(TriaxialModel):
    pass
