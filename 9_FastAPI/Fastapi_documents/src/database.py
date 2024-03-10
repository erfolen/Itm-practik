from config import data_base_url
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

async_engine = create_async_engine(data_base_url(), echo=True)
async_session_fabric = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
