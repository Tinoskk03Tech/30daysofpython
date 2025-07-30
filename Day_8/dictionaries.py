# 1. Créer un dictionnaire vide appelé dog
dog = {}

# 2. Ajouter le nom, la couleur, la race, le nombre de pattes et l'âge au dictionnaire dog
dog['name'] = 'Rex'
dog['color'] = 'Marron'
dog['breed'] = 'Berger Allemand'
dog['legs'] = 4
dog['age'] = 5

# 3. Créer un dictionnaire étudiant
student = {
    'first_name': 'Kossivi',
    'last_name': 'Tine',
    'gender': 'Masculin',
    'age': 18,
    'marital_status': 'Célibataire',
    'skills': ['Python', 'C'],
    'country': 'Togo',
    'city': 'Lomé',
    'address': '12 Rue Lumière, Lomé'
}

# 4. Obtenir la longueur du dictionnaire student
print("Longueur du dictionnaire étudiant :", len(student))

# 5. Obtenir la valeur de skills et vérifier le type de données
skills = student['skills']
print("Compétences :", skills)
print("Type de compétences :", type(skills))

# 6. Modifier skills en ajoutant de nouvelles compétences
student['skills'].append('SQL')
student['skills'].extend(['HTML', 'CSS'])

# 7. Obtenir les clés du dictionnaire sous forme de liste
print("Clés :", list(student.keys()))

# 8. Obtenir les valeurs du dictionnaire sous forme de liste
print("Valeurs :", list(student.values()))

# 9. Convertir le dictionnaire en liste de tuples
print("Éléments sous forme de tuples :", list(student.items()))

# 10. Supprimer un élément du dictionnaire (par exemple, address)
del student['address']
print("Après suppression :", student)

# 11. Supprimer complètement le dictionnaire dog
del dog
# print(dog)  # provoque une erreur si décommenté