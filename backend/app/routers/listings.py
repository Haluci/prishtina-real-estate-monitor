
from fastapi import APIRouter
from app.database import get_conn

router = APIRouter(prefix="/listings", tags=["Listings"])

@router.get("/")
def get_all():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM listings ORDER BY created_at DESC")
    rows = c.fetchall()
    conn.close()
    return rows
