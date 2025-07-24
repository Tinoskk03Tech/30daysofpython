#Question 1

print("Python 3.13.5") #python --version
# Affichage de la version de Python
import sys
print("La version de Python est : ", sys.version)

#Question 2

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)


#Question 3
print("My lastname : Kossivi Tinè")
print("My firstname : KOSSI")
print("My Country is Togo")
print("I enjoy of 30 days of python")

#Question 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 + 4j))
print(type(['Asabeneh', 'Python', 'Finlande']))
print(type("Kossivi Tinè"))
print(type("KOSSI"))
print(type("Togo"))


#### Exercice 3
#Question 1

a = 15 #entier
b = 20.5 #float
c = 5 + 7j #complexe
d = "Python" #string
e = True #boolean
f = [15, 20, 30] #list
g = (15, 20, 30) #tuple
h = {15, 20, 30} #set
i = {'name': 'Kossivi', 'age': 18} #dictionnaire

#Question 2

import math
# Coordonnées des deux points
point1 = (2, 3)
point2 = (10, 8)
# Calcul de la distance euclidienne
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
# Affichage du résultat
print(f"La distance euclidienne entre {point1} et {point2} est : {distance:.2f}")
