
from playwright.sync_api import sync_playwright
import time

def scrape_group():
    url = "https://www.facebook.com/groups/503238920436051"
    listings = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(url, timeout=60000)
        time.sleep(5)

        for _ in range(6):
            page.mouse.wheel(0, 2500)
            time.sleep(2)

        posts = page.query_selector_all("div[role='article']")
        for post in posts:
            try:
                text = post.inner_text()
                listings.append({"description": text})
            except:
                continue

        browser.close()
    return listings
