# Backend (FastAPI)

This is a minimal FastAPI app scaffold for JD7Co eSIM platform.

How to run locally:

1. Create a virtualenv: python -m venv .venv
2. Activate and install: pip install -r requirements.txt
3. Run: uvicorn main:app --reload --host 0.0.0.0 --port 8000

Docker:
- See Dockerfile

Endpoints:
- GET /health
- GET /esim/profiles
- GET /partners

