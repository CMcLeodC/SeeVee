from fastapi import FastAPI

app = FastAPI(title="CV Portfolio API", description="AI-powered CV query backend")

@app.get("/")
async def root():
    return {"message": "Welcome to the CV Portfolio API"}

@app.post("/query")
async def query_endpoint(query: dict):
    # Placeholder for LangChain/Supabase logic
    return {
        "response": "This is a placeholder response",
        "data": [],
        "display_hint": "text"
    }