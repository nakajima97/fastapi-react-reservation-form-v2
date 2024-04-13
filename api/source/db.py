from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://root@mysql:3306/reservation_form"
ASYNC_DB_URL = "mysql+aiomysql://root@mysql:3306/reservation_form"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=async_engine,
  class_=AsyncSession
)

Base = declarative_base()

async def get_db():
  async with async_session() as session:
    yield session