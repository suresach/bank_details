import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

URL = 'https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009'
OUTPUT_DIR = '.'

open_url = urlopen(URL)
try:
    html = open_url.read().decode('utf-8')
finally:
    open_url.close()

soup = BeautifulSoup(html, "html.parser")
for link in soup.select('a[href^="http://"]'):
    href = link.get('href')
    if not any(href.endswith(x) for x in ['.csv','.xls','.xlsx']):
        continue

    filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])
    href = href.replace('http://','https://')
    urlretrieve(href, filename)
    print("Download Complete")

