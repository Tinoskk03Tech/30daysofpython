# Données initiales
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 🔹 Level 1

# 1. Longueur du set it_companies
print("1:", len(it_companies))

# 2. Ajouter 'Twitter'
it_companies.add('Twitter')
print("2:", it_companies)

# 3. Ajouter plusieurs entreprises
it_companies.update(['Cisco', 'Nvidia', 'HP'])
print("3:", it_companies)

# 4. Supprimer une entreprise
it_companies.remove('Oracle')  # ou discard
print("4:", it_companies)

# 5. Différence entre remove et discard
# remove génère une erreur si l’élément n’existe pas, discard ne génère pas d’erreur.
try:
    it_companies.remove('TikTok')  # provoque une erreur
except KeyError:
    print("5: remove → erreur si l'élément n'existe pas")
it_companies.discard('TikTok')     # ne provoque pas d’erreur
print("5: discard → aucune erreur même si l’élément n’existe pas")

## 🔹 Level 2

# 1. Union de A et B
print("6:", A.union(B))

# 2. Intersection
print("7:", A.intersection(B))

# 3. Est-ce que A est un sous-ensemble de B ?
print("8:", A.issubset(B))

# 4. A et B sont-ils disjoints ?
print("9:", A.isdisjoint(B))

# 5. A ∪ B et B ∪ A
print("10:", A.union(B))
print("10bis:", B.union(A))

# 6. Différence symétrique
print("11:", A.symmetric_difference(B))

# 7. Supprimer totalement les sets
del A
del B
# print(A)  # provoque une erreur si décommenté

# 🔹 Level 3

# 1. Convertir âge en set et comparer les longueurs
ages_set = set(age)
print("12: Longueur liste =", len(age), "| Longueur set =", len(ages_set))

# 2. Différences entre types
print("13: string → séquence de caractères (immutable)")
print("13: list → collection ordonnée (mutable)")
print("13: tuple → collection ordonnée (immutable)")
print("13: set → collection non ordonnée, sans doublons (mutable, non indexable)")

# 3. Compter les mots uniques
phrase = "I am a teacher and I love to inspire and teach people"
unique_words = set(phrase.split())
print("14: Mots uniques dans la phrase =", len(unique_words))