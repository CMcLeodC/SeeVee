from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def create_engine_and_session(database_url: str):
    connect_args = {
        "statement_cache_size": 0,
        "server_settings": {"application_name": "SeeVee"}
    }

    print("Engine connect_args:", connect_args)

    engine = create_async_engine(
        database_url,
        echo=True,
        connect_args=connect_args,
        pool_pre_ping=True,
        execution_options={"compiled_cache": None},
    )

    print("Using engine with statement_cache_size = 0")

    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    return engine, async_session

