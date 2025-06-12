from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Supabase PostgreSQL connection
DATABASE_URL = os.getenv("SUPABASE_URL")
engine = None  # Initialize later in lifespan

def init_engine():
    global engine
    if engine is None:
        engine = create_async_engine(
            DATABASE_URL,
            echo=True,
            connect_args={
                "statement_cache_size": 0,
                "prepared_statement_cache_size": 0,
                "server_settings": {"application_name": "SeeVee"},
                "command_timeout": 30
            },
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10
        )

def get_sessionmaker():
    if engine is None:
        init_engine()
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    session_factory = get_sessionmaker()
    async with AsyncSession(engine) as session:
        yield session
        await session.close()