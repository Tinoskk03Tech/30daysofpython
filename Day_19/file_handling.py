import json
import re
from collections import Counter

# -------------------------------
# Level 1 - Exercice 1 : Compter lignes et mots dans un fichier texte
def count_lines_and_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.splitlines()
        words = re.findall(r'\b\w+\b', content)
    return len(lines), len(words)

print("1:")
files = [
    './data/obama_speech.txt',
    './data/michelle_obama_speech.txt',
    './data/donald_speech.txt',
    './data/melina_trump_speech.txt'
]

for f in files:
    try:
        lines, words = count_lines_and_words(f)
        print(f"{f} → {lines} lines, {words} words")
    except FileNotFoundError:
        print(f"{f} not found.")

# -------------------------------
# Level 1 - Exercice 2 : 10 langues les plus parlées
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    lang_counter = Counter()
    for country in data:
        for lang in country.get('languages', []):
            lang_counter[lang] += 1
    return lang_counter.most_common(top_n)

print("\n2:")
try:
    print(most_spoken_languages('./data/countries_data.json', 10))
    print(most_spoken_languages('./data/countries_data.json', 3))
except FileNotFoundError:
    print("countries_data.json not found.")

# -------------------------------
# Level 1 - Exercice 3 : 10 pays les plus peuplés
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    sorted_data = sorted(
        data,
        key=lambda x: x.get('population', 0),
        reverse=True
    )
    return [
        {'country': c.get('name', 'Unknown'), 'population': c.get('population', 0)}
        for c in sorted_data[:top_n]
    ]

print("\n3:")
try:
    print(most_populated_countries('./data/countries_data.json', 10))
    print(most_populated_countries('./data/countries_data.json', 3))
except FileNotFoundError:
    print("countries_data.json not found.")

# -------------------------------
# Level 2 - Exercice 4 : Extraire les adresses email
def extract_emails(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', content)
    return emails

print("\n4:")
try:
    email_list = extract_emails('./data/email_exchange_big.txt')
    print("Emails found:", email_list[:10])  # Affiche les 10 premiers
except FileNotFoundError:
    print("email_exchange_big.txt not found.")

# -------------------------------
# Level 2 - Exercice 5 : Mots les plus fréquents
def find_most_common_words(filepath, top_n):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    words = re.findall(r'\b[a-z]+\b', text)
    freq = Counter(words)
    return freq.most_common(top_n)

print("\n5:")
try:
    print(find_most_common_words('./data/sample.txt', 10))
    print(find_most_common_words('./data/sample.txt', 5))
except FileNotFoundError:
    print("sample.txt not found.")