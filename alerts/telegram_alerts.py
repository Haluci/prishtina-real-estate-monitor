
import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        return "Missing Telegram credentials"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, data=payload)
    return r.status_code

def send_daily_summary(listings):
    if not listings:
        return send_telegram_message("No new listings today.")
    msg = "🔥 Daily Real Estate Summary (Prishtina)\n\n"
    for l in listings[:10]:
        msg += f"• €{l['price']} | {l['size_m2']} m² | {l['location']} | Scam: {l['scam_score']}\n"
    return send_telegram_message(msg)
