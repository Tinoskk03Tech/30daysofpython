# 1. Declaration d'un entier age
age = 18

# 2. Declaration d'une variable taille float
taille = 1.70

# 3. Declaration d'une variable complexe
nbre_complexe = 3 + 4j

# 4. Calcul de la zone d'un triangle
base = float(input("\nEntrez la base du triangle : "))
hauteur = float(input("Entrez la hauteur du triangle : "))
zone_triangle = 0.5 * base * hauteur
print("La zone du triangle est : ", zone_triangle)

# 5. Clacul du perimetre d'un triangle
cote_A = float(input("\nEntrez la longueur du côté A : "))
cote_B = float(input("Entrez la longueur du côté B : "))
cote_C = float(input("Entrez la longueur du côté C : "))
perimetre_triangle = cote_A + cote_B + cote_C
print("Le périmètre du triangle est : ", perimetre_triangle)

import math
# 6. Surface et perimetre d'un rectangle
longueur = float(input("\nEntrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
surface_rectangle = longueur * largeur
perimetre_rectangle = 2 * (longueur + largeur)
print("La surface du rectangle est : ", surface_rectangle)

# 7. Calcul de la zone et circonférence d'un cercle
rayon = float(input("\nEntrez le rayon du cercle : "))
zone_cercle = math.pi * (rayon ** 2)
circonference_cercle = 2 * math.pi * rayon
print("La zone du cercle est : ", zone_cercle)
print("La circonférence du cercle est : ", circonference_cercle)

# 8. Slope, x intercept, y intercept
print("\nÉquation : y = 2x - 2")
slope = 2
x_intercept = 2 / slope
y_intercept = -2 
print("Pente =", slope)
print("X-intercept =", x_intercept)
print("Y-intercept =", y_intercept)

# 9. Pente et distance euclidienne entre (2, 2) et (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pente = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("\nPente entre les deux points =", pente)
print("Distance euclidienne =", distance)

# 10. Comparaison des pentes
print("\nComparaison :")
print("Pente de l’équation = 2")
print("Pente des points = {:.2f}".format(pente))

# 11. Résolution de y = x^2 + 6x + 9
print("\nÉquation : y = x² + 6x + 9")
for x in range(-5, 5):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
print("La valeur qui donne y = 0 est x = -3")

# 12. Comparaison de Python et Dragon
mot1 = "Python"
mot2 = "Dragon"
print("\nLongueur de ", mot1, " : ", len(mot1))
print("Longueur de ", mot2, " : ", len(mot2))
print("Comparaison de la longueur de ", mot1, " et ", mot2, " : ", len(mot1) == len(mot2))

# 13. Verifions si le mot 'on' est dans 'dragon' et 'python'
resultat_and = ("on" in mot1) and ("on" in mot2)
print("\nLe mot 'on' est-il dans 'Python' et 'Dragon' ? :", resultat_and)

# 14. Verifions que 'jargon' est dans notre phrase
phrase = "\nI hope this course is not full of jargon."
resultat_jargon = "jargon" in phrase
print("Le mot 'jargon' est-il dans la phrase ? :", resultat_jargon)

# 15. Verifions que 'on' n'est pas dans 'python' et 'dragon'
resultat_not_in = ("on" not in mot1) and ("on" not in mot2)
print("\nLe mot 'on' n'est-il pas dans 'Python' et 'Dragon' ? :", resultat_not_in)

# 16. Longueur du texte 'Python' et conversion de cette longueur
texte = "Python"
longueur_texte = len(texte)
longueur_texte_float = float(longueur_texte)
longueur_texte_str = str(longueur_texte)
print("\nLongueur de 'Python' :", longueur_texte, 
      "en float :", longueur_texte_float, 
      "et en string :", longueur_texte_str)

# 17. Verifions si le nombre est divisible par 2
nombre = int(input("\nEntrez un nombre pour vérifier s'il est divisible par 2 : "))
if nombre % 2 == 0:
    print("Le nombre", nombre, "est divisible par 2.")
else:
    print("Le nombre", nombre, "n'est pas divisible par 2.")
    
# 18. Verifications de la division plancher et convertion
division_plancher = 7 // 3
nombre_int = int(2.7)
print("\nLa division entière de 7 par 3 est :", division_plancher)
print("Le nombre 2,7 converti en entier est :", nombre_int)
print("Egalite entre nos deux valeurs pecedent : ", division_plancher == nombre_int)

# 19. Comparons le type de 10 et "10"
print("\nLe type de 10 est :", type(10))
print("Le type de '10' est :", type("10"))
print("Sont-ils égaux ? :", type(10) == type("10"))

# 20. Comparons int(9.8) et 10
print("\nLa conversion de 9.8 en entier donne :", int(9.8))
print("Est-ce égal à 10 ? :", int(9.8) == 10)

# 21. Calcul de la renumeration de l'utilisateur
nb_heure = input("\nEntrez le nombre d'heures : ")
taux_horaire = input("Entrez le taux horaire : ")
renumeration = float(nb_heure) * float(taux_horaire)
print("Votre rémunération s'eleve de :", renumeration)

# 22. Calcul du temps vecu en secondes par l'utilisateur
temps_vecu = int(input("\nEntrez votre temps de vie en années : "))
temps_vecu_secondes = temps_vecu * 365 * 24 * 60 * 60
print("Votre temps de vie en secondes est :", temps_vecu_secondes)

# 23. Affichage d'un tableau structure
print("\n1 1 1 1 1 2 1 2 4")
print("8 3 1 3 9 27 4 1 4 1")
print("6 64 5 1 5 25 125\n")