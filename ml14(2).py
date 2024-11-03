import requests
from bs4 import BeautifulSoup
import json
def count_word_occurrences(url, word):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        count = text.lower().count(word.lower())
        return count
    except requests.exceptions.RequestException as e:
        print(f"Помилка при обробці URL {url}: {e}")
        return None
def save_results_to_json(results, filename="news.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)
urls = []
while True:
    url = input("Введіть URL: ")
    if url.lower() == 'q':
        break
    urls.append(url)
results = {}
for url in urls:
    count = count_word_occurrences(url, "Ukraine")
    if count is not None:
        results[url] = count
    else:
        results[url] = "Error retrieving data"    
    save_results_to_json(results)
    print("Результати збережено у файлі news.json")
