# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Feature

DATABASE_URL = "sqlite:///features.db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL queries
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Create tables
Base.metadata.create_all(bind=engine)

# Function to add a feature
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

# Function to get a feature (latest version by default)
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

def connect_db():
    # Just to show database connection works
    print("Database connected successfully")
