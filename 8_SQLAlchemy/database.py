import os
from decimal import Decimal
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Numeric
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Annotated

# # Подключение к серверу MySQL на localhost с помощью PyMySQL DBAPI.
# engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")
# # Подключение к серверу MySQL по ip 23.92.23.113 с использованием mysql-python DBAPI.
# engine = create_engine("mysql+mysqldb://root:pass@23.92.23.113/mydb")
# # Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
# engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")
# # Подключение к серверу Oracle на локальном хосте с помощью cx-Oracle DBAPI.
# engine = create_engine("oracle+cx_oracle://root:pass@localhost/mydb"))
# # Подключение к MSSQL серверу на localhost с помощью PyODBC DBAPI.
# engine = create_engine("oracle+pyodbc://root:pass@localhost/mydb")

# engine = create_engine("postgresql+psycopg2://test_2:password@localhost/test_2")
# engine = create_engine("postgresql+psycopg2://test_2:password@localhost/test_2")


load_dotenv()
login = os.getenv("user_database")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
host = os.getenv("HOST")

engine = create_engine(f"postgresql+psycopg2://{login}:{password}@{host}/{database}", echo=True)
session_fabric = sessionmaker(engine)

str_150 = Annotated[str, 150]
str_15 = Annotated[str, 15]
num_12_2 = Annotated[Decimal, 12]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_150: String(200),
        str_15: String(15),
        num_12_2: Numeric(12, 2)
    }
