from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")