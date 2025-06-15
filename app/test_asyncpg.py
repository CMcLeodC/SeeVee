import asyncio
import asyncpg

url = "postgresql://postgres.ryyskfzwktcqjznlhtda:bump2025BuMP@aws-0-eu-west-2.pooler.supabase.com:6543/postgres"

async def main():
    conn = await asyncpg.connect(url, statement_cache_size=0)
    result = await conn.fetch("SELECT * FROM job_history LIMIT 1")
    print(result)
    await conn.close()

asyncio.run(main())
