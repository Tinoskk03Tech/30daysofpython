# 🔹 LEVEL 1

# 1. Iterate 0 to 10 using for and while
print("Exercice 1:")
for i in range(11):
    print(i)

print("\nWhile loop:")
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Iterate 10 to 0 using for and while
print("\nExercice 2:")
for i in range(10, -1, -1):
    print(i)

print("\nWhile loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Triangle pattern
print("\nExercice 3:")
for i in range(1, 8):
    print('#' * i)

# 4. Nested loop pattern
print("\nExercice 4:")
for _ in range(8):
    print('# ' * 8)

# 5. Multiplication pattern
print("\nExercice 5:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through tech list
print("\nExercice 6:")
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)

# 7. Print even numbers from 0 to 100
print("\nExercice 7:")
for i in range(0, 101, 2):
    print(i)

# 8. Print odd numbers from 0 to 100
print("\nExercice 8:")
for i in range(1, 101, 2):
    print(i)

# 🔹 LEVEL 2

# 1. Sum of all numbers from 0 to 100
print("\nLevel 2 - Exercice 1:")
total = sum(range(101))
print("The sum of all numbers is", total)

# 2. Sum of evens and odds
print("\nLevel 2 - Exercice 2:")
sum_even = sum(i for i in range(101) if i % 2 == 0)
sum_odd = sum(i for i in range(101) if i % 2 != 0)
print("The sum of all evens is", sum_even)
print("The sum of all odds is", sum_odd)

# 🔹 LEVEL 3

# 1. Extract countries containing 'land'
print("\nLevel 3 - Exercice 1:")
try:
    from data.countries import countries
    land_countries = [country for country in countries if 'land' in country]
    print("Countries containing 'land':", land_countries)
except ImportError:
    print("⚠️ Le fichier countries.py est introuvable.")

# 2. Reverse fruit list using loop
print("\nLevel 3 - Exercice 2:")
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruits:", reversed_fruits)

# 3. Countries data analysis
print("\nLevel 3 - Exercice 3:")
try:
    from data.countries_data import countries_data

    # i. Total number of unique languages
    languages = []
    for country in countries_data:
        languages.extend(country['languages'])
    unique_languages = set(languages)
    print("Total number of languages:", len(unique_languages))

    # ii. Ten most spoken languages
    from collections import Counter
    language_counter = Counter(languages)
    most_spoken = language_counter.most_common(10)
    print("Ten most spoken languages:")
    for lang, count in most_spoken:
        print(f"{lang}: {count}")

    # iii. Ten most populated countries
    sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    top_10_populated = [country['name'] for country in sorted_by_population[:10]]
    print("Ten most populated countries:")
    for country in top_10_populated:
        print(country)

except ImportError:
    print("⚠️ Le fichier countries_data.py est introuvable.")
