from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")

Session = sessionmaker(engine)
