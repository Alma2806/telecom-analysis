import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.telekom.de/mobilfunk/tarife"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

data = []

# Scraping pravi
packages = soup.find_all("div", class_="package")

for package in packages:
    try:
        name = package.find("h2").text.strip()
        price = package.find("span", class_="price").text.strip()
        speed = "N/A"
        data.append({
            "package": name,
            "price": price,
            "speed": speed,
            "country": "Germany",
            "operator": "Telekom.de"
        })
    except:
        continue

df = pd.DataFrame(data)
df.to_csv("./data/telekom_de_mobile.csv", index=False)
print("✅ Scraping complete. Saved to /data.")


import pandas as pd

# Kreiranje jednostavnog testnog DataFrame-a
data = {
    'Operator': ['Telekom', 'Vodafone', 'O2'],
    'Price_EUR': [39.99, 29.99, 34.99],
    'Data_GB': [20, 10, 15]
}

df = pd.DataFrame(data)

df.to_csv("data/telekom_de_mobile.csv", index=False)

print("CSV fajl je uspješno kreiran!")

import os

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)  # Kreira folder ako ne postoji
output_path = os.path.join(output_dir, "telekom_de_mobile.csv")

df.to_csv(output_path, index=False)





