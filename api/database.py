from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environs import Env

env = Env()
env.read_env()

engine = create_engine(
    env.str('DB_STRING'),
    pool_size=100,
    max_overflow=10,
    pool_recycle=3600,
    pool_timeout=30,
    connect_args={'connect_timeout': 60},
    isolation_level='READ UNCOMMITTED')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
