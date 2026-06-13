from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="JD7Co eSIM Platform - Backend")

class ESIMProfile(BaseModel):
    id: str
    name: str
    operator: str
    data_mb: int

class Partner(BaseModel):
    id: str
    name: str
    commission_percent: float

# In-memory stubs for initial scaffold
profiles_db = [
    {"id": "p1", "name": "Global 1GB", "operator": "ExampleNet", "data_mb": 1024},
]
partners_db = [
    {"id": "partner_jd7", "name": "JD7Co Partner", "commission_percent": 10.0}
]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/esim/profiles", response_model=List[ESIMProfile])
async def list_profiles():
    return profiles_db

@app.get("/partners", response_model=List[Partner])
async def list_partners():
    return partners_db

@app.post("/esim/profiles")
async def create_profile(profile: ESIMProfile):
    # Placeholder: validate and store
    profiles_db.append(profile.dict())
    return profile

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
