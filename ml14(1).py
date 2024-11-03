import json
import requests
from bs4 import BeautifulSoup
from collections import Counter

with open("countries.txt", "r", encoding="utf-8") as file:
  countries = [line.strip() for line in file]
with open("web.txt", "r", encoding="utf-8") as file:
  urls = [line.strip() for line in file]

country_count = Counter()

for url in urls:
  try:
    page = requests.get(url)
    page.raise_for_status()
    content = page.text.lower()
    for country in countries:
      count = content.count(country.lower())
      if count > 0:
        country_count[country] += count
  except requests.RequestException as error:
    print(f"Не вдалося отримати дані з однієї із сторінки: {error}")

top_3 = country_count.most_common(3)

list_json = [{"country":country , "mentions": count} for country, count in top_3]
list_json = [f"{country}: {count}" for country, count in top_3]
with open("top_3.json", "w", encoding="utf-8") as file:
    json.dump(list_json, file, ensure_ascii=False, indent=4)
print("Завдання виконано!")

  

    



