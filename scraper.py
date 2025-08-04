import requests
from bs4 import BeautifulSoup
import re

url = "https://exemplo.com"  # Substitua pelo site real

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

telefones = re.findall(r'\(?\d{2}\)?\s?\d{4,5}[-.\s]?\d{4}', soup.text)

for telefone in set(telefones):
    print(telefone)
