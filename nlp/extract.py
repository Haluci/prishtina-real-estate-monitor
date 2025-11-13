
import re

def extract_size(text):
    m = re.search(r"(\d{2,3})\s?m2", text.lower())
    return float(m.group(1)) if m else None

def extract_floor(text):
    m = re.search(r"kati\s?(\d+)", text.lower())
    return int(m.group(1)) if m else None

def extract_heating(text):
    patterns = ["termokos","nxemje","bojler","inverter","qendrore"]
    for p in patterns:
        if p in text.lower():
            return p
    return None

def extract_location(text):
    zones = ["ulipiana","uliana","dardani","mati","kalabria","arberi","qender"]
    for z in zones:
        if z in text.lower():
            return z
    return None

def extract_all(raw):
    return {
        "size_m2": extract_size(raw),
        "floor": extract_floor(raw),
        "heating": extract_heating(raw),
        "location": extract_location(raw)
    }
