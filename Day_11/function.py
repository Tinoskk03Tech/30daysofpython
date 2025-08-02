import math
from collections import Counter

# 🔹 Level 1
print('Exercice Level 1')

# 1. Addition de deux nombres
def add_two_numbers(a, b):
    return a + b  # Retourne la somme de a et b
print(add_two_numbers(1, 2)) # -> 3

# 2. Aire d’un cercle
def area_of_circle(r):
    return math.pi * r * r  # Aire = π × r²
print(area_of_circle(2))

# 3. Addition d’un nombre arbitraire d’arguments
def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    return "Erreur : tous les éléments doivent être numériques."
print(add_all_nums(1, 2, 3))

# 4. Conversion Celsius → Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Formule standard
print(convert_celsius_to_fahrenheit(42))

# 5. Déterminer la saison selon le mois
def check_season(month):
    month = month.lower()
    seasons = {
        'automne': ['september', 'october', 'november'],
        'hiver': ['december', 'january', 'february'],
        'printemps': ['march', 'april', 'may'],
        'été': ['june', 'july', 'august']
    }
    for saison, mois in seasons.items():
        if month in mois:
            return saison.capitalize()
    return "Mois invalide"
print(check_season('august'))

# 6. Calcul de la pente d’une droite
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Pente indéfinie (ligne verticale)"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4))

# 7. Résolution d’une équation quadratique
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Pas de racines réelles"
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2
print(solve_quadratic_eqn(1, 2, 3))

# 8. Impression des éléments d’une liste
def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3])

# 9. Inversion d’une liste avec boucle
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
print(reverse_list([1, 2, 3]))

# 10. Capitalisation des éléments d’une liste
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]
print(capitalize_list_items([1,2,3]))

# 11. Ajout d’un élément à la fin d’une liste
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item([1,2,3], 'apple'))

# 12. Suppression d’un élément d’une liste
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print(remove_item([1,2,3], 'apple'))

# 13. Somme des nombres jusqu’à n
def sum_of_numbers(n):
    return sum(range(n + 1))
print(sum_of_numbers(5))

# 14. Somme des nombres impairs jusqu’à n
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)
print(sum_of_odds(5))

# 15. Somme des nombres pairs jusqu’à n
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
print(sum_of_even(5))

# 🔹 Level 2
print('Exercice Level 2')

# 1. Compter les nombres pairs et impairs jusqu’à n
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"Nombre de pairs : {evens}, Nombre d'impairs : {odds}"
print(evens_and_odds(5))

# 2. Factorielle d’un nombre
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))

# 3. Vérifier si une variable est vide
def is_empty(value):
    return value == "" or value == [] or value == {} or value is None
print(is_empty(5))

# 4. Moyenne d’une liste
def calculate_mean(lst):
    return sum(lst) / len(lst)
print(calculate_mean([15, 18, 17, 16]))

# 5. Médiane d’une liste
def calculate_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    return lst[mid]
print(calculate_median([1,2,3]))

# 6. Mode d’une liste
def calculate_mode(lst):
    freq = Counter(lst)
    max_count = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_count]
    return mode
print(calculate_mode([1,2,3]))

# 7. Étendue d’une liste
def calculate_range(lst):
    return max(lst) - min(lst)
print(calculate_range([1,2,3]))

# 8. Variance
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean)**2 for x in lst) / len(lst)
print(calculate_variance([1,2,3]))

# 9. Écart-type
def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
print(calculate_std([1,2,3]))

# 🔹 Level 3
print('Exercice Level 3')

# 1. Vérifier si un nombre est premier
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

# 2. Vérifier unicité des éléments
def all_unique(lst):
    return len(lst) == len(set(lst))
print(all_unique([1,2,3]))

# 3. Vérifier si tous les éléments ont le même type
def same_type(lst):
    return all(type(x) == type(lst[0]) for x in lst)
print(same_type([1,2,3]))

# 4. Vérifier si une variable est un nom Python valide
def is_valid_variable(name):
    return name.isidentifier()
print(is_valid_variable('Kossivi'))

# 5. Analyse des données de pays (fichier externe requis)
# Simulé ici avec un exemple fictif
countries_data = [
    {'country': 'China', 'population': 1400000000, 'languages': ['Chinese']},
    {'country': 'India', 'population': 1380000000, 'languages': ['Hindi', 'English']},
    {'country': 'USA', 'population': 330000000, 'languages': ['English']},
    # ... autres pays
]
print(countries_data)

def most_spoken_languages(data, top_n=10):
    lang_counter = Counter()
    for country in data:
        lang_counter.update(country['languages'])
    return lang_counter.most_common(top_n)
print(most_spoken_languages(countries_data))

def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]
print(most_populated_countries(countries_data))
