from functools import reduce

# Données de base
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 🔹 Level 1

# 1. Différence entre map, filter, reduce
print("1: map → transforme chaque élément\n   filter → sélectionne selon condition\n   reduce → agrège tous les éléments")

# 2. Différence entre higher-order function, closure, decorator
print("2: higher-order → prend ou retourne une fonction\n   closure → fonction interne qui mémorise l’environnement\n   decorator → modifie le comportement d’une fonction")

# 3. Fonction de rappel
def square(x):
    return x * x

# 4. Afficher chaque pays
print("\n4:")
for country in countries:
    print(country)

# 5. Afficher chaque nom
print("\n5:")
for name in names:
    print(name)

# 6. Afficher chaque nombre
print("\n6:")
for number in numbers:
    print(number)

# 🔹 Level 2

# 1. Pays en majuscules
print("\n7:")
upper_countries = list(map(str.upper, countries))
print(upper_countries)

# 2. Carrés des nombres
print("\n8:")
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# 3. Noms en majuscules
print("\n9:")
upper_names = list(map(str.upper, names))
print(upper_names)

# 4. Pays contenant 'land'
print("\n10:")
land_countries = list(filter(lambda c: 'land' in c, countries))
print(land_countries)

# 5. Pays avec exactement 6 caractères
print("\n11:")
six_char_countries = list(filter(lambda c: len(c) == 6, countries))
print(six_char_countries)

# 6. Pays avec 6 lettres ou plus
print("\n12:")
six_or_more = list(filter(lambda c: len(c) >= 6, countries))
print(six_or_more)

# 7. Pays commençant par 'E'
print("\n13:")
starts_with_e = list(filter(lambda c: c.startswith('E'), countries))
print(starts_with_e)

# 8. Chaining map + filter + reduce
print("\n14:")
result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print("Sum of even squares:", result)

# 9. get_string_lists
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

print("\n15:")
mixed = ['Python', 123, True, 'C++', None]
print(get_string_lists(mixed))

# 10. reduce pour somme
print("\n16:")
total_sum = reduce(lambda x, y: x + y, numbers)
print("Total sum:", total_sum)

# 11. reduce pour concaténation
print("\n17:")
sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + f", and {countries[-1]} are north European countries"
print(sentence)

# 12. categorize_countries
def categorize_countries(pattern):
    return [c for c in countries if pattern in c]

print("\n18:")
print("Countries with 'land':", categorize_countries('land'))
print("Countries with 'ia':", categorize_countries('ia'))

# 13. Dictionnaire par lettre initiale
def country_letter_count(country_list):
    result = {}
    for country in country_list:
        first = country[0]
        result[first] = result.get(first, 0) + 1
    return result

print("\n19:")
print(country_letter_count(countries))

# 14. get_first_ten_countries
def get_first_ten_countries(country_list):
    return country_list[:10]

print("\n20:")
print(get_first_ten_countries(countries))

# 15. get_last_ten_countries
def get_last_ten_countries(country_list):
    return country_list[-10:]

print("\n21:")
print(get_last_ten_countries(countries))

# 🔹 Level 3

# 1. Analyse avec countries_data
try:
    from Day_10.data.countries_data import countries_data

    # a. Trier par nom
    sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
    print("\n22a: Sorted by name:", [c['name'] for c in sorted_by_name[:5]])

    # b. Trier par capitale
    sorted_by_capital = sorted(countries_data, key=lambda x: x.get('capital', ''))
    print("22b: Sorted by capital:", [c.get('capital', '') for c in sorted_by_capital[:5]])

    # c. Trier par population
    sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    print("22c: Top 5 by population:", [f"{c['name']} ({c['population']})" for c in sorted_by_population[:5]])

    # d. 10 langues les plus parlées
    from collections import Counter
    all_langs = []
    for country in countries_data:
        all_langs.extend(country['languages'])
    lang_counter = Counter(all_langs)
    top_langs = lang_counter.most_common(10)
    print("22d: Most spoken languages:")
    for lang, count in top_langs:
        print(f"{lang}: {count}")

    # e. 10 pays les plus peuplés
    top_populated = sorted_by_population[:10]
    print("22e: Most populated countries:")
    for country in top_populated:
        print(f"{country['name']}: {country['population']}")

except ImportError:
    print("⚠️ Le fichier countries_data.py est introuvable.")
