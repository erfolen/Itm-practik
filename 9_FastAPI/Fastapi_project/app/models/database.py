from config_my import login, password, host, database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(f"postgresql+psycopg2://{login}:{password}@{host}/{database}", echo=True)
session_fabric = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


print(login, password, host, database)
