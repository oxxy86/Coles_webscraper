import requests
from bs4 import BeautifulSoup

URL = "https://www.coles.com.au/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="search-text-input")
print(results.prettify())