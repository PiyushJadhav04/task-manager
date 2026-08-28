# this is for database connection/setup 

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

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
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="tasks")

# Table for Project Category 
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    tasks = relationship("Task", back_populates="project")

# Initialize Database Tables
def init_db():
    Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
