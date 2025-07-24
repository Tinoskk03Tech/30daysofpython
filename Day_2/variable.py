# Jour 2 : 30 Days of Python Programming

# Question 1
prenom = "Kossivi Tinè"
nom_famille = "KOSSI"
nom_complet = prenom + " " + nom_famille
pays = "Togo"
municipale = "Agoe-Nyivé 1"
an = 2025
est_Married = False
is_True = True
IS_light_on = True

x, y, z = "Python", 3.13, True


# Question 2
# Affichage des types des variables
print("Le type de la variable prenom est : ", type(prenom))
print("Le type de la variable nom_famille est : ", type(nom_famille))
print("Le type de la variable nom_complet est : ", type(nom_complet))
print("Le type de la variable pays est : ", type(pays))
print("Le type de la variable municipale est : ", type(municipale))
print("Le type de la variable an est : ", type(an))
print("Le type de la variable est_Married est : ", type(est_Married))
print("Le type de la variable is_True est : ", type(is_True))
print("Le type de la variable IS_light_on est : ", type(IS_light_on))
print("Le type de la variable x est : ", type(x))
print("Le type de la variable y est : ", type(y))
print("Le type de la variable z est : ", type(z))
print()
print("La longueur de la variable prenom est : ", len(prenom))
print("Comparaison des variables prenom avec nom de famille : ", prenom == nom_famille)

# Declaration de variables
num_one = 5
num_two = 4

addition = num_one + num_two

soustraction = num_one - num_two

multiplication = num_one * num_two

division = num_one / num_two

reste = num_one % num_two

division_entier = num_one // num_two

# Affichage des résultats
print()
print("Résultats des opérations sur num_one et num_two :")
print("Addition de num_one et num_two : ", addition)
print("Soustraction de num_one et num_two : ", soustraction)
print("Multiplication de num_one et num_two : ", multiplication)
print("Division de num_one et num_two : ", division)
print("Reste de la division de num_one par num_two : ", reste)
print("Division entière de num_one par num_two : ", division_entier)


# Question 3 
import math
print()
print("Calcul de la zone et de la circonférence d'un cercle")
royon = 30
# Cacul de la zone d'un cercle
area_of_circle = math.pi * (royon ** 2)
print("La zone d'un cercle de rayon ", royon, " est : ", area_of_circle)
# Cacul de la circonférence d'un cercle
circum_of_circle = 2 * math.pi * royon
print("La circonférence d'un cercle de rayon ", royon, " est : ", circum_of_circle)
# Recuperation du rayon de l'utilisateur
user_royon = float(input("Entrez le rayon du cercle : "))
# Cacul de la zone d'un cercle avec le rayon de l'utilisateur
user_area_of_circle = math.pi * (user_royon ** 2)
print("La zone d'un cercle de rayon ", user_royon, " est : ", user_area_of_circle)

# Question 4
print()
print("Veullez entrer vos informations : ")
user_prenom = input("Entrez votre prénom : ")
user_nom_famille = input("Entrez votre nom de famille : ")
user_pays = input("Entrez votre pays : ")
user_age = int(input("Entrez votre âge : "))


# Affichage des informations de l'utilisateur
print()
print("Les informations sur l'utilisateur sont : ")
print("Votre prénom est : ", user_prenom)
print("Votre nom de famille est : ", user_nom_famille)
print("Votre pays est : ", user_pays)
print("Votre âge est : ", user_age)


# Question 5
import keyword
# Liste des mots clés réservés
print()
print(keyword.kwlist)