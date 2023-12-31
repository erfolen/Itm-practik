import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import create_engine


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

class DB_test:

    def __init__(self, database, host, login, password):
        self.engine = create_engine(f"postgresql+psycopg2://{login}:{password}@{host}/{database}")
        self.engine.connect()



if __name__ == '__main__':
    test_2 = DB_test(database, host, login, password)
    print(test_2.engine)
    print(login)