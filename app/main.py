from fastapi import FastAPI, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse
from app.db.database import create_engine_and_session
from app.db.queries.job_history import get_job_history
from app.db.queries.chat_history import save_chat_history
from app.db.queries.users import get_user
from app.db.queries.projects import get_projects
from app.db.queries.education import get_education
from app.db.queries.skills import get_skills
from app.schemas.job_history import JobHistorySchema
from app.schemas.query import QueryInput
from app.schemas.response import QueryResponse
from app.schemas.users import UserSchema
from app.schemas.projects import ProjectSchema
from app.schemas.education import EducationSchema
from app.schemas.skills import SkillSchema
from app.llm.llm_config import classify_query, summarize_data
from typing import List
import logging

load_dotenv()
DATABASE_URL = os.getenv("SUPABASE_URL")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

async def get_db(request: Request):
    # Try to get from app state
    session_factory = getattr(request.app.state, "session_factory", None)

    # Fallback for Vercel or environments without lifespan
    if session_factory is None:
        from os import getenv
        from dotenv import load_dotenv
        load_dotenv()
        DATABASE_URL = getenv("SUPABASE_URL")
        _, session_factory = create_engine_and_session(DATABASE_URL)

    async with session_factory() as session:
        yield session

@app.get("/")
async def root():
    return {"message": "Welcome to the CV Portfolio API"}

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(query_input: QueryInput, db: AsyncSession = Depends(get_db)):
    try:
        intent = classify_query(query_input.query)
        user_id = "b4fceb51-aaf8-4de7-a209-0a38d730c61d"

        data = []
        response_text = "Sorry, I don't understand that query yet."
        display_hint = "text"

        if intent == "jobs":
            jobs = await get_job_history(db, user_id)
            data = [JobHistorySchema.from_orm(job).dict() for job in jobs]
            response_text = summarize_data(data, field="description")
            display_hint = "timeline"

        elif intent == "projects":
            projects = await get_projects(db, user_id)
            data = [ProjectSchema.from_orm(project).dict() for project in projects]
            response_text = summarize_data(data, field="description")
            display_hint = "table"

        elif intent == "education":
            education = await get_education(db, user_id)
            data = [EducationSchema.from_orm(edu).dict() for edu in education]
            response_text = summarize_data(data, field="description")
            display_hint = "timeline"

        elif intent == "skills":
            skills = await get_skills(db, user_id)
            data = [SkillSchema.from_orm(skill).dict() for skill in skills]
            response_text = summarize_data(data, field="name")  # If no description, use name
            display_hint = "list"

        elif intent == "profile":
            user = await get_user(db, user_id)
            data = [UserSchema.from_orm(user).dict()] if user else []
            response_text = summarize_data(data, field="bio")  # Adjust field as needed
            display_hint = "text"

        await save_chat_history(db, user_id, query_input.query, response_text)

        return QueryResponse(
            response=response_text,
            data=data,
            display_hint=display_hint
        )

    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return QueryResponse(
            response="An error occurred while processing your query.",
            data=[],
            display_hint="text"
        )

@app.get("/job_history", response_model=List[JobHistorySchema])
async def get_job_history_endpoint(user_id: str, db: AsyncSession = Depends(get_db)):
    try:
        jobs = await get_job_history(db, user_id)
        if not jobs:
            logger.info(f"No job history found for user_id: {user_id}")
        return jobs
    except Exception as e:
        logger.error(f"Error fetching job history: {str(e)}")
        return []
