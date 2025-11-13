
import math

ZONE_PRICES = {
    "ulipiana": 1550,
    "ulpiana": 1550,
    "dardani": 1450,
    "qender": 1700,
    "arberi": 1500,
    "kalabria": 1200,
    "mati": 1150,
    "mati 1": 1150,
    "mati1": 1150,
}

def base_zone_price(location: str):
    if not location: 
        return 900
    for z, p in ZONE_PRICES.items():
        if z in location.lower():
            return p
    return 900

def fair_value_prediction(size_m2, location, floor, heating):
    if not size_m2:
        return None

    base = size_m2 * base_zone_price(location)

    floor_factor = 1.0
    if floor in [2,3,4]:
        floor_factor = 1.05
    elif floor and floor > 7:
        floor_factor = 0.95

    heating_factor = 1.0
    if heating == "termokos":
        heating_factor = 1.06
    elif heating in ["bojler", "inverter"]:
        heating_factor = 0.97

    predicted = base * floor_factor * heating_factor
    return round(predicted, 2)

def price_fairness(actual_price, predicted_price):
    if not actual_price or not predicted_price:
        return None

    diff = actual_price - predicted_price
    pct = diff / predicted_price * 100

    if abs(pct) <= 10:
        return "Fair"
    elif pct < -10:
        return "Undervalued"
    else:
        return "Overvalued"

def price_score(actual_price, predicted_price):
    if not actual_price or not predicted_price:
        return 0

    fairness = price_fairness(actual_price, predicted_price)
    if fairness == "Undervalued":
        return 90
    if fairness == "Fair":
        return 75
    return 40
