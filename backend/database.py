# this is for database connection/setup 

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///tasks.db"

# sets up connection and where to locate the database file
engine = create_engine(DATABASE_URL)

# Configure session and model base
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Database model 
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    done = Column(Boolean, nullable=False)


# Initialize Database Tables
def init_db():
    Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
