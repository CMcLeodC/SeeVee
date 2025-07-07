from fastapi import Request
from app.db.database import create_engine_and_session
from dotenv import load_dotenv
from os import getenv
import os

load_dotenv()

async def get_db(request: Request):
    session_factory = getattr(request.app.state, "session_factory", None)

    if session_factory is None:
        DATABASE_URL = getenv("SUPABASE_URL")
        _, session_factory = create_engine_and_session(DATABASE_URL)

    async with session_factory() as session:
        yield session
