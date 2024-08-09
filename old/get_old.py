import requests_cache
import bs4
import xml.etree.ElementTree
import simpletimer

DATE_TAG = "{http://www.pbcore.org/PBCore/PBCoreNamespace.html}pbcoreAssetDate"
PER_PAGE = 100


def scrapePage(page_number):
    timer = simpletimer.Timer()
    timer.start()

    # DNS caching is faster
    # Probably could be faster with expiration settings
    session = requests_cache.CachedSession()
    page_response = session.get(
        f"https://americanarchive.org/catalog?f[access_types][]=online&sort=asset_date+asc&per_page={PER_PAGE}&page={page_number}"
    )

    page_soup = bs4.BeautifulSoup(page_response.text, "html.parser")
    table = page_soup.find(class_="documents-list")

    date_strings = []

    # while this: scrape page

    # Iterate through table rows for record links
    for row in table.find_all(class_="document"):
        record_link = row.find("a")["href"]
        # GET and parse
        xml_response = session.get(f"https://americanarchive.org{record_link}.pbcore")
        root = xml.etree.ElementTree.fromstring(xml_response.content)

        date_element = root.find(DATE_TAG)
        if date_element is None:
            print("first undated record")
            return False
            # Break here
        date_strings.append(date_element.text)
        # Parse this =...

    for date_string in date_strings:
        out.write(date_string + "\n")
    # Assuming 00 is unknown month or unknown day
    # All of these have year though, so first look at that
    timer.end()
    print(page_number, ":", timer.elapsed())
    return True


out = open("./dates", "w")

# Sorting by oldest ensures that all dated records appear first
# Count up how many dated records there are = ((per_page * "fully dated pages") + "dated on last page") / "available online"
page_number = 1
while True:
    result = scrapePage(page_number)
    if not result:
        break
    page_number += 1


out.close()


import requests

response = requests.get(
    "https://americanarchive.org/api.xml?q=asimov&fl=id,title,xml&rows=3&start=5"
)

print(response.text)
