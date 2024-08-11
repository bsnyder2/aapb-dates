import requests_cache
import xml.etree.ElementTree
import simpletimer

DATE_TAG = "{http://www.pbcore.org/PBCore/PBCoreNamespace.html}pbcoreAssetDate"
# "all"/"digitized"/"online"
ACCESS_TYPE = "online"
# Right now ~485,000 dated records
PER_QUERY = 100
QUERIES = 4900
START = 0

session = requests_cache.CachedSession()
file = open("years-online.tsv", "w+")

years = []
for query_i in range(QUERIES):
    # Sorting by asset_date field ensures that all dated records appear first
    response = session.get(
        f"https://americanarchive.org/api.xml?fl=xml&fq=access_types:{ACCESS_TYPE}&sort=asset_date%20asc&rows={PER_QUERY}&start={PER_QUERY * (query_i + START)}"
    )
    root = xml.etree.ElementTree.fromstring(response.content)
    records = root.findall("./response/docs/doc/xml")
    for record_i, record in enumerate(records):
        subroot = xml.etree.ElementTree.fromstring(record.text)
        date_element = subroot.find(DATE_TAG)
        if date_element is None:
            print(f"first undated record in query {query_i}")
            exit()
        year = date_element.text[:4]
        file.write(f"{query_i}\t{record_i}\t{year}\n")

file.close()
