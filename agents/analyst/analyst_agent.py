from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI()
BACKEND_URL = "http://localhost:9000"

class CaseData(BaseModel):
    scheme: str
    status: str
    stated_reason: str
    cert_issue_date: str
    issuing_authority: str
    family_income: int
    income_proof_type: str

@app.post("/analyse")
async def analyse(case_data: CaseData):
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BACKEND_URL}/analyse", json=case_data.model_dump())
        return r.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)