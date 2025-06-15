from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def create_engine_and_session(database_url: str):
    engine = create_async_engine(
        database_url,
        echo=True,
        connect_args={
            "statement_cache_size": 0,
            "server_settings": {"application_name": "SeeVee"}
        },
        pool_pre_ping=True,
        # This disables SQLAlchemy's internal compiled cache
        execution_options={"compiled_cache": None},
    )

    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    return engine, async_session
