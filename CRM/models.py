from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy_utils import database_exists, create_database

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'
DB_NAME = 'crm'

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

class Contract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    signed_date = Column(DateTime, nullable=True)
    status = Column(String, default="черновик")
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)
    project = relationship('Project', foreign_keys='Contract.project_id', backref='contracts')


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()


