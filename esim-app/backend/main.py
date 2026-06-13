from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

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
    referral_url: Optional[str] = None
    partner_code: Optional[str] = None

class ConversionEvent(BaseModel):
    amount_usd: float
    timestamp: Optional[datetime] = None

class Report(BaseModel):
    partner_id: str
    clicks: int
    conversions: int
    revenue_usd: float
    estimated_commission_usd: float

# In-memory stubs for initial scaffold
profiles_db = [
    {"id": "p1", "name": "Global 1GB", "operator": "ExampleNet", "data_mb": 1024},
]

# Partners include referral_url placeholders — публично в репо. Замените на реальные URL позже.
partners_db = [
    {
        "id": "airalo",
        "name": "Airalo",
        "commission_percent": 10.0,
        "referral_url": "https://airalo.com/?ref=JD7CO_AIRALO",
        "partner_code": "JD7_AIRALO"
    },
    {
        "id": "nomad",
        "name": "Nomad",
        "commission_percent": 8.0,
        "referral_url": "https://getnomad.app/?ref=JD7CO_NOMAD",
        "partner_code": "JD7_NOMAD"
    },
]

# Simple in-memory analytics store
analytics_store = {
    # partner_id: {"clicks": int, "conversions": int, "revenue_usd": float}
}

@app.on_event("startup")
async def startup_init():
    for p in partners_db:
        analytics_store[p["id"]] = {"clicks": 0, "conversions": 0, "revenue_usd": 0.0}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/esim/profiles", response_model=List[ESIMProfile])
async def list_profiles():
    return profiles_db

@app.post("/esim/profiles")
async def create_profile(profile: ESIMProfile):
    profiles_db.append(profile.dict())
    return profile

@app.get("/partners", response_model=List[Partner])
async def list_partners():
    return partners_db

@app.post("/partners/{partner_id}/click")
async def register_click(partner_id: str = Path(..., description="Partner id")):
    if partner_id not in analytics_store:
        raise HTTPException(status_code=404, detail="Partner not found")
    analytics_store[partner_id]["clicks"] += 1
    return {"status": "ok", "partner_id": partner_id, "clicks": analytics_store[partner_id]["clicks"]}

@app.post("/partners/{partner_id}/conversion")
async def register_conversion(partner_id: str, event: ConversionEvent):
    if partner_id not in analytics_store:
        raise HTTPException(status_code=404, detail="Partner not found")
    # record conversion
    analytics_store[partner_id]["conversions"] += 1
    analytics_store[partner_id]["revenue_usd"] += event.amount_usd
    return {"status": "ok", "partner_id": partner_id, "conversions": analytics_store[partner_id]["conversions"]}

@app.get("/partners/{partner_id}/reports", response_model=Report)
async def get_report(partner_id: str):
    if partner_id not in analytics_store:
        raise HTTPException(status_code=404, detail="Partner not found")
    partner = next((p for p in partners_db if p["id"] == partner_id), None)
    if not partner:
        raise HTTPException(status_code=404, detail="Partner metadata not found")
    stats = analytics_store[partner_id]
    est_commission = stats["revenue_usd"] * (partner.get("commission_percent", 0.0) / 100.0)
    return Report(
        partner_id=partner_id,
        clicks=stats["clicks"],
        conversions=stats["conversions"],
        revenue_usd=round(stats["revenue_usd"], 2),
        estimated_commission_usd=round(est_commission, 2)
    )

@app.post("/partners/register")
async def register_partner(name: str):
    # simple partner registration (demo). In production — validations, auth, persistent DB.
    pid = name.lower().replace(" ", "_") + "_" + uuid4().hex[:6]
    partner = {
        "id": pid,
        "name": name,
        "commission_percent": 5.0,
        "referral_url": f"https://example.com/?ref=JD7CO_{pid.upper()}",
        "partner_code": f"JD7_{pid.upper()}"
    }
    partners_db.append(partner)
    analytics_store[pid] = {"clicks": 0, "conversions": 0, "revenue_usd": 0.0}
    return partner
