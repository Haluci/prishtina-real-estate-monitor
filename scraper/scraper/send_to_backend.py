
import requests

BACKEND_URL = "http://127.0.0.1:8000/listings"

def send_listing(data):
    try:
        r = requests.post(BACKEND_URL, json=data)
        return r.status_code
    except:
        return None
