## Exercice 1
# 1. Créer un tuple vide
empty_tuple = ()
print("Tuple vide :", empty_tuple)

# 2. Créer un tuple de sœurs et de frères
sisters = ("Florence", "Ormélia", "Paméla")
brothers = ("Wisdon", "Boris", "Raphael")
print("Sœurs :", sisters)
print("Frères :", brothers)

# 3. Joindre les frères et les sœurs
siblings = sisters + brothers
print("Frères et sœurs :", siblings)

# 4. Compter le nombre de frères et sœurs
print("Nombre de frères et sœurs :", len(siblings))

# 5. Ajouter les parents au tuple des frères et sœurs
family_members = siblings + ("Papa", "Maman")
print("Membres de la famille :", family_members)

## Exercice 2
# 1. Déballer les frères/sœurs et les parents à partir de family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print("Frères et sœurs :", siblings)
print("Parents :", parents)

# 2. Créer des tuples et les joindre
fruits = ('Pomme', 'Banane', 'Mangue')
vegetables = ('Tomate', 'Carotte', 'Oignon')
animal_products = ('Lait', 'Œufs', 'Fromage')
food_stuff_tp = fruits + vegetables + animal_products
print("Nourriture (tuple) :", food_stuff_tp)

# 3. Convertir le tuple en liste
food_stuff_lt = list(food_stuff_tp)
print("Nourriture (liste) :", food_stuff_lt)

# 4. Extraire l’/les élément(s) du milieu
length = len(food_stuff_lt)
if length % 2 == 0:
    print("Éléments du milieu :", food_stuff_lt[length//2 - 1:length//2 + 1])
else:
    print("Élément du milieu :", food_stuff_lt[length//2])

# 5. Extraire les trois premiers et les trois derniers éléments
print("3 premiers éléments :", food_stuff_lt[:3])
print("3 derniers éléments :", food_stuff_lt[-3:])

# 6. Supprimer complètement le tuple
del food_stuff_tp
# print(food_stuff_tp) # Provoquerait une erreur si décommenté

# 7. Vérifier si des éléments existent dans le tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("L'Estonie est-elle nordique ?", 'Estonia' in nordic_countries)
print("L'Islande est-elle nordique ?", 'Iceland' in nordic_countries)