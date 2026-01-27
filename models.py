from sqlalchemy import Column, Integer, String, Float
from database import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True)
    entity_id = Column(String)
    feature_name = Column(String)
    version = Column(String)
    value = Column(Float)
