
from marketplace_scraper import scrape_marketplace
from group_scraper import scrape_group
from send_to_backend import send_listing

def run_all():
    mp = scrape_marketplace()
    gr = scrape_group()

    for item in mp:
        send_listing(item)
    for item in gr:
        send_listing(item)

if __name__ == "__main__":
    run_all()
