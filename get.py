import requests
from requests_cache import CachedSession
from bs4 import BeautifulSoup

import lxml
import time


# Simple timer
class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def elapsed(self):
        return self.end_time - self.start_time


per_page = 100

# DNS caching is 300x faster nice
session = CachedSession(expire_after=600)
# timer = Timer()
# timer.start()


# TODO: while records are dated- all pages

# Sorting by oldest ensures that all dated records appear first
# Count up how many dated records there are = ((per_page * "fully dated pages") + "dated on last page") / "available online"
first_page = f"https://americanarchive.org/catalog?f[access_types][]=online&per_page={per_page}&sort=asset_date+asc"


page_response = requests.get(first_page)
page_soup = BeautifulSoup(page_response.text, "html.parser")
rows = page_soup.find(class_="documents-list")


# Iterate through records for links
for row in rows.find_all(class_="document"):
    record_link = row.find("a")["href"]
    # possible to do xml request instead of http?
    xml_response = session.get(f"https://americanarchive.org{record_link}.pbcore")
    print(xml_response.status_code)
    # ...


# timer.end()
# print(timer.elapsed())
