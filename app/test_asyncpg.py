import asyncio
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("SUPABASE_URL")

async def main():
    conn = await asyncpg.connect(DATABASE_URL, statement_cache_size=0)
    result = await conn.fetch("SELECT * FROM job_history LIMIT 1")
    print(result)
    await conn.close()

asyncio.run(main())
