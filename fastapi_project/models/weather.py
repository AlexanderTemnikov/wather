from sqlalchemy import  Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

weather_table = Table(
    "weather",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("city", String(20)),
    Column("year", Integer),
    Column("month", String(10)),
    Column("temperature", Float(10)),
)


# class Weather(Base):
#     __tablename__ = "weather"
#     id = Column(Integer, primary_key=True, autoincrement=True),
#     City = Column(String(10)),
#     Years = Column(Integer)
#     Months = Column(String(10))
#     Temperature = Column(Float)






