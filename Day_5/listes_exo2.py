# Exercices sur l'âge des étudiants
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Trier et trouver le min, le max
ages.sort()
print("Âges triés :", ages)
print("Âge minimum :", min(ages))
print("Âge maximum :", max(ages))

# 2. Ajouter à nouveau le min et le max à la liste
ages.append(min(ages))
ages.append(max(ages))
print("Âges mis à jour :", ages)

# 3. Trouver la médiane
ages.sort()
length = len(ages)
if length % 2 == 0:
    median = (ages[length//2 - 1] + ages[length//2]) / 2
else:
    median = ages[length//2]
print("Médiane :", median)

# 4. Trouver la moyenne
average = sum(ages) / len(ages)
print("Moyenne :", average)

# 5. Trouver l'étendue
age_range = max(ages) - min(ages)
print("Étendue des âges :", age_range)

# 6. Comparer (min - moyenne) et (max - moyenne)
print("Différence avec le min :", abs(min(ages) - average))
print("Différence avec le max :", abs(max(ages) - average))

# Exercices sur la liste des pays
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# 1. Trouver le(s) pays du milieu
mid = len(countries) // 2
if len(countries) % 2 == 0:
    print("Pays du milieu :", countries[mid-1:mid+1])
else:
    print("Pays du milieu :", countries[mid])

# 2. Diviser en deux moitiés égales
first_half = countries[:(len(countries)+1)//2]
second_half = countries[(len(countries)+1)//2:]
print("Première moitié :", first_half)
print("Deuxième moitié :", second_half)

# 3. Déballer les 3 premiers et le reste comme pays nordiques
country1, country2, country3, *scandic_countries = countries
print("Trois premiers pays :", country1, country2, country3)
print("Pays nordiques :", scandic_countries)