# 1. Déclaration d'une liste vide
empty_list = []

# 2. Déclarer une liste avec plus de 5 éléments
items = ['Stylo', 'Cahier', 'Téléphone', 'Chargeur', 'Sac', 'Ordinateur', 'Souris']

# 3. Trouver la longueur de la liste
print(len(items))

# 4. Obtenir le premier, le milieu et le dernier élément de la liste
print(items[0])                      # Premier
print(items[len(items)//2])          # Milieu
print(items[-1])                     # Dernier

# 5. Déclarer une liste de types de données mixtes
mixed_data_types = ['Kossivi', 18, 1.70, 'Célibataire', 'Lomé, Togo']

# 6. Déclarer la liste des entreprises informatiques
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Afficher la liste
print(it_companies)

# 8. Afficher le nombre d'entreprises
print(len(it_companies))

# 9. Afficher la première, celle du milieu et la dernière entreprise
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Modifier le nom d'une entreprise
it_companies[2] = 'Meta'
print(it_companies)

# 11. Ajouter une entreprise informatique
it_companies.append('Tencent')
print(it_companies)

# 12. Insérer une entreprise au milieu
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'SAP')
print(it_companies)

# 13. Mettre un nom en majuscule (sauf IBM)
for i in range(len(it_companies)):
    if it_companies[i] != 'IBM':
        it_companies[i] = it_companies[i].upper()
        break
print(it_companies)

# 14. Joindre les entreprises avec '#; '
print('#; '.join(it_companies))

# 15. Vérifier si une entreprise existe
print('Google' in it_companies)

# 16. Trier la liste
it_companies.sort()
print(it_companies)

# 17. Inverser la liste
it_companies.reverse()
print(it_companies)

# 18. Extraire les 3 premières entreprises
print(it_companies[:3])

# 19. Extraire les 3 dernières entreprises
print(it_companies[-3:])

# 20. Extraire l'entreprise ou les entreprises du milieu
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(it_companies[mid-1:mid+1])  # Nombre pair : 2 du milieu
else:
    print([it_companies[mid]])        # Nombre impair : 1 du milieu

# 21. Supprimer la première entreprise
it_companies.pop(0)
print(it_companies)

# 22. Supprimer l'entreprise ou les entreprises du milieu
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[mid-1:mid+1]
else:
    del it_companies[mid]
print(it_companies)

# 23. Supprimer la dernière entreprise
it_companies.pop()
print(it_companies)

# 24. Supprimer toutes les entreprises
it_companies.clear()
print(it_companies)

# 25. Détruire la liste
del it_companies
# print(it_companies)  # Décommenter ceci provoquera une erreur

# 26. Joindre front_end et back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
stack = front_end + back_end
print(stack)

# 27. Copier la liste jointe, insérer Python & SQL après Redux
full_stack = stack.copy()
index_redux = full_stack.index('Redux')
full_stack[index_redux + 1:index_redux + 1] = ['Python', 'SQL']