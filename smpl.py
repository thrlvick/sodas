import os
import requests
from bs4 import BeautifulSoup

url = "https://example.com/products"

response = requests.get(url)

soup = BeautifulSoup(response.tetx, 'html.parser')

for item in soup,find_all('h2'):
    print(item.text.strip())')

