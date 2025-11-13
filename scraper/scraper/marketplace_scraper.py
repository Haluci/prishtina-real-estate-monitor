
from playwright.sync_api import sync_playwright
import time, re

def extract_price(text):
    m = re.search(r"(\d+[\.,]?\d*)", text.replace(",", "").replace(".", ""))
    return float(m.group(1)) if m else None

def scrape_marketplace():
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.facebook.com/marketplace/prishtina/search/?query=banesa", timeout=60000)
        time.sleep(5)

        for _ in range(8):
            page.mouse.wheel(0, 2500)
            time.sleep(1.5)

        posts = page.query_selector_all("div[role='article']")
        for post in posts:
            try:
                link = post.query_selector("a").get_attribute("href")
                text = post.inner_text()
                price = extract_price(text)
                results.append({"url": link, "price": price, "raw_text": text})
            except:
                continue

        browser.close()
    return results
