
import re
import math

SUSPICIOUS_KEYWORDS = [
    "urgent", "deposit", "parapagim", "send money", "no viewing",
    "owner abroad", "trust me", "cheap", "too good", "scam"
]

def keyword_score(text):
    t = text.lower()
    score = sum(1 for k in SUSPICIOUS_KEYWORDS if k in t)
    return score * 10

def price_anomaly_score(actual_price, predicted_price):
    if not actual_price or not predicted_price:
        return 0
    if actual_price < predicted_price * 0.5:
        return 40
    if actual_price < predicted_price * 0.7:
        return 25
    return 0

def text_structure_score(text):
    if len(re.findall(r'\n', text)) < 1:
        return 10
    return 0

def scam_probability(text, actual_price, predicted_price):
    score = 0
    score += keyword_score(text)
    score += price_anomaly_score(actual_price, predicted_price)
    score += text_structure_score(text)
    return min(score, 100)
