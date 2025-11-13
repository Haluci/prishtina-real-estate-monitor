
import os
import json
from datetime import datetime
from alerts.telegram_alerts import send_daily_summary

def load_daily_listings():
    if not os.path.exists("daily_listings.json"):
        return []
    with open("daily_listings.json", "r") as f:
        return json.load(f)

def run_daily_alerts():
    listings = load_daily_listings()
    send_daily_summary(listings)
    print(f"[{datetime.now()}] Alerts sent successfully.")
