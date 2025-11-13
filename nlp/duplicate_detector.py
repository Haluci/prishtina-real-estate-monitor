
import hashlib

def listing_hash(text):
    return hashlib.md5(text.lower().encode()).hexdigest()
