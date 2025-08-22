from sqlalchemy import Column, Integer, Float, String, Date, Time
from database import Base

class WeatherForecast(Base):
    __tablename__ = "weather_forecast"

    id = Column(Integer, primary_key=True, index=True)
    base_date = Column(Date)
    base_time = Column(Time)
    fcst_date = Column(Date)
    fcst_time = Column(Time)
    category = Column(String(10))
    value = Column(String(10))
    nx = Column(Integer)
    ny = Column(Integer)

class HeatShelter(Base):
    __tablename__ = "heatwave_shelters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    address = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
