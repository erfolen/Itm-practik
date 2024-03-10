import os

from dotenv import load_dotenv

load_dotenv()
login = os.getenv("user_database")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
host = os.getenv("HOST")


def data_base_url():
    return f'postgresql+asyncpg://{login}:{password}@{host}/{database}'


def data_base_url_sync():
    return f'postgresql+psycopg2://{login}:{password}@{host}/{database}'
