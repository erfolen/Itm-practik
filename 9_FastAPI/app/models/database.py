import os
from decimal import Decimal
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Numeric
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Annotated

load_dotenv()
login = os.getenv("user_database")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
host = os.getenv("HOST")

engine = create_engine(f"postgresql+psycopg2://{login}:{password}@{host}/{database}", echo=True)
session_fabric = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
