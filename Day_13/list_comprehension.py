# 💻 Day 13 – Skill Foundry Exercises

# 1️⃣ Filtrer les nombres négatifs et zéro
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [n for n in numbers if n <= 0]
print("1.", neg_and_zero)  # ➜ [-4, -3, -2, -1, 0]

# 2️⃣ Aplatir une liste de listes de listes
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print("2.", flattened)  # ➜ [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3️⃣ Créer une liste de tuples avec des puissances
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("3.")
for t in tuple_list:
    print(t)

# 4️⃣ Transformer une liste de pays en liste enrichie
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [[country.upper(), country[:3].upper(), city.upper()]
                  for group in countries for (country, city) in group]
print("4.", flat_countries)
# ➜ [['FINLAND','FIN','HELSINKI'], ['SWEDEN','SWE','STOCKHOLM'], ['NORWAY','NOR','OSLO']]

# 5️⃣ Transformer en liste de dictionnaires
country_dicts = [{'country': country.upper(), 'city': city.upper()}
                 for group in countries for (country, city) in group]
print("5.", country_dicts)
# ➜ [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]

# 6️⃣ Liste de chaînes concaténées
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for group in names for (first, last) in group]
print("6.", full_names)
# ➜ ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7️⃣ Lambda pour calculer la pente ou l'ordonnée à l'origine
# Forme générale : y = mx + b
# Pour la pente : (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - m * x

# Exemple :
print("7a. Slope:", slope(1, 2, 3, 6))         # ➜ (6 - 2) / (3 - 1) = 2.0
print("7b. Y-intercept:", y_intercept(2, 6, 2))  # ➜ 6 - 2*2 = 2