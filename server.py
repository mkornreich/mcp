from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from logger import logger

mcp = FastMCP("ashby")

# Constants
ASHBY_URL = "https://api.ashbyhq.com/posting-api/job-board/moonshot-ai?includeCompensation=true"

async def make_ashby_request(url: str) -> dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def get_jobs() -> str:
    data = await make_ashby_request(ASHBY_URL)
    jobs = data["jobs"]
    return str(jobs)

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
