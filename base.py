from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgres://postgres:1111@localhost:5432/postgres')
Session = sessionmaker(bind=engine)

Base = declarative_base()
