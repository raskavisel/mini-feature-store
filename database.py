# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///features.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def connect_db():
    print("Database connected successfully")

# Import models here, AFTER Base is created
from models import Feature

# Create tables
Base.metadata.create_all(bind=engine)

def add_feature(entity_id, feature_name, value, version="1"):
    db: Session = SessionLocal()
    feature = Feature(
        entity_id=entity_id,
        feature_name=feature_name,
        version=version,
        value=value
    )
    db.add(feature)
    db.commit()
    db.close()
    print(f"Feature '{feature_name}' added for entity '{entity_id}' version {version}")

def get_feature(entity_id, feature_name, version=None):
    db: Session = SessionLocal()
    query = db.query(Feature).filter(Feature.entity_id==entity_id, Feature.feature_name==feature_name)
    if version:
        query = query.filter(Feature.version==version)
    result = query.order_by(Feature.version.desc()).first()
    db.close()
    if result:
        return result.value
    else:
        return None
