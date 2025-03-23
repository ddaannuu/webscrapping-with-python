import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.kompas.com/"
response = requests.get(url)
soup=BeautifulSoup(response.content, "html.parser")

berita_container=soup.find_all("h1", class_="hlTitle")

with open("berita.csv", 'w', newline="", encoding="utf-8")as csv_file:
    writer=csv.writer(csv_file)

    for i,container in enumerate(berita_container, start=1):
        berita=f"{i}.{container.get_text(strip=True)}"
        writer.writerow([berita])
