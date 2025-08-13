import requests
from bs4 import BeautifulSoup
import json
import os

# 📁 Créer un dossier pour stocker les fichiers JSON
os.makedirs('day22_outputs', exist_ok=True)

# 🔹 1. Scraper Boston University Facts & Stats
def scrape_bu_facts():
    url = 'http://www.bu.edu/president/boston-university-facts-stats/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    facts = {}
    for section in soup.find_all('div', class_='facts-container'):
        for item in section.find_all(['h3', 'p']):
            key = item.get_text(strip=True)
            value = item.find_next_sibling('p')
            if value:
                facts[key] = value.get_text(strip=True)

    with open('day22_outputs/bu_facts_stats.json', 'w', encoding='utf-8') as f:
        json.dump(facts, f, indent=4, ensure_ascii=False)

# 🔹 2. Extraire le tableau des datasets UCI
def scrape_uci_datasets():
    url = 'https://archive.ics.uci.edu/ml/datasets.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.find_all('table')
    dataset_table = tables[4]  # Basé sur la structure actuelle

    datasets = []
    for row in dataset_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) >= 5:
            dataset = {
                'Name': cols[0].get_text(strip=True),
                'Data Types': cols[1].get_text(strip=True),
                'Default Task': cols[2].get_text(strip=True),
                'Attribute Types': cols[3].get_text(strip=True),
                'Instances': cols[4].get_text(strip=True)
            }
            datasets.append(dataset)

    with open('day22_outputs/uci_datasets.json', 'w', encoding='utf-8') as f:
        json.dump(datasets, f, indent=4, ensure_ascii=False)

# 🔹 3. Scraper la liste des présidents des États-Unis
def scrape_us_presidents():
    url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})
    presidents = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all(['th', 'td'])
        if len(cols) >= 4:
            president = {
                'Number': cols[0].get_text(strip=True),
                'Name': cols[1].get_text(strip=True),
                'Term': cols[2].get_text(strip=True),
                'Party': cols[3].get_text(strip=True)
            }
            presidents.append(president)

    with open('day22_outputs/us_presidents.json', 'w', encoding='utf-8') as f:
        json.dump(presidents, f, indent=4, ensure_ascii=False)

# 🚀 Exécution des trois fonctions
if __name__ == '__main__':
    print("Scraping Boston University Facts...")
    scrape_bu_facts()
    print("Scraping UCI Datasets...")
    scrape_uci_datasets()
    print("Scraping US Presidents...")
    scrape_us_presidents()
    print("✅ All data scraped and saved in 'day22_outputs/' folder.")
