
from fastapi import FastAPI
from app.routers import listings
from app.database import init_db

app = FastAPI(title="Prishtina Real Estate Monitor - Backend")

init_db()
app.include_router(listings.router)

@app.get("/")
def root():
    return {"status": "backend running"}
