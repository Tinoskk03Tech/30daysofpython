import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
from bs4 import BeautifulSoup

# 📁 Dossier de sortie
output_dir = "/mnt/data"

# --- 1. Roméo et Juliette (Gutenberg) ---
url_text = "http://www.gutenberg.org/files/1112/1112.txt"
text = requests.get(url_text).text
start = text.find("ACT I")
text = text[start:]
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)
top_10 = word_counts.most_common(10)
print("📘 Top 10 mots fréquents dans Roméo et Juliette :", top_10)

# --- 2. Cats API ---
url_cats = "https://api.thecatapi.com/v1/breeds"
cats_data = requests.get(url_cats).json()
cats = []
for cat in cats_data:
    try:
        weight = float(cat['weight']['metric'].split(' ')[0])
        lifespan = int(cat['life_span'].split(' ')[0])
        cats.append({
            'name': cat['name'],
            'origin': cat['origin'],
            'weight': weight,
            'lifespan': lifespan
        })
    except:
        continue
df_cats = pd.DataFrame(cats)
print("\n🐱 Statistiques sur les races de chats :")
print(df_cats.describe())
print("\nOrigines les plus fréquentes :")
print(df_cats['origin'].value_counts().head())

# --- 3. Countries API ---
url_countries = "https://restcountries.com/v3.1/all"
countries_data = requests.get(url_countries).json()
countries = []
for country in countries_data:
    try:
        name = country['name']['common']
        area = country.get('area', 0)
        langs = list(country.get('languages', {}).values())
        countries.append({'name': name, 'area': area, 'languages': langs})
    except:
        continue
df_countries = pd.DataFrame(countries)
print("\n🌍 10 plus grands pays par superficie :")
print(df_countries.nlargest(10, 'area')[['name', 'area']])
all_langs = [lang for langs in df_countries['languages'] for lang in langs]
print("\n🗣️ Langues uniques :", set(all_langs))

# --- 4. UCI Datasets ---
url_uci = "https://archive.ics.uci.edu/ml/datasets.php"
html = requests.get(url_uci).text
soup = BeautifulSoup(html, 'html.parser')
datasets = [a.text.strip() for a in soup.select('table a') if a.text.strip()]
print("\n📊 Nombre total de jeux de données UCI :", len(datasets))
print("Exemples :", datasets[:10])
