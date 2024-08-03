import requests
import lxml
from bs4 import BeautifulSoup
import time


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


from requests_cache import CachedSession

# DNS caching is 300x faster
session = CachedSession(expire_after=600)

per_page = 100

foo = f"https://americanarchive.org/catalog?f[access_types][]=online&per_page={per_page}&sort=asset_date+asc"


bar = requests.get(foo)
baz = BeautifulSoup(bar.text, "html.parser")
rows = baz.find(class_="documents-list")


timer = Timer()
timer.start()

docs = []

# how fast?


# docs = [row.find("a")["href"] for row in rows.find_all(class_="document")]
# bar = current.find_all(class_="document")

# print(bar[0])

# docs2 = []
# print(len(docs))

for row in rows.find_all(class_="document"):
    record_link = row.find("a")["href"]
    response = session.get(f"https://americanarchive.org{record_link}.pbcore")
    print(response.status_code)

# docs3 = []

timer.end()
print(timer.elapsed())

# Iterate through documents-list

# Sorting by oldest ensures that all dated records appear first
# Count up how many dated records there are = ((per_page * "fully dated pages") + "dated on last page") / "available online"

# start = time.time()
# print(start)
# zz = requests.get("https://americanarchive.org/catalog/cpb-aacip_80-644qs701.pbcore")
# print()
