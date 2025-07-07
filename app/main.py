from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api import query_routes, job_history_routes  # import any others
from app.db.database import create_engine_and_session
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("SUPABASE_URL")

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine, session_factory = create_engine_and_session(DATABASE_URL)
    app.state.engine = engine
    app.state.session_factory = session_factory
    yield
    await engine.dispose()

app = FastAPI(
    title="CV Portfolio API",
    description="AI-powered CV query backend",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(query_routes.router)
app.include_router(job_history_routes.router)
