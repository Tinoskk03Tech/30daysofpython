## Exemple 1 : Synthase error
print('\n Synthase error')
#print 'Hello World' # Provoque des erreurs lié au syntaxe
print('Hello World')  # Correct syntax

## Exemple 2 : NameError
print('\n Name error')
# print(age)  # Provoque une erreur car age n'est pas défini
age = 18 
print(age)  # Correct, age est défini

## Exemple 3 : IndexError
print('\n Index error')
numbers = [ 1, 2, 3, 4, 5 ]
# print(numbers[5])  # Provoque une erreur car l'index 5 n'existe pas
print(numbers[4])  # Correct, l'index 4 existe ou # print(numbers[-1])  # Correct, l'index -1 accède au dernier élément

## Exemple 4 : ModuleNotFoundError
print('\n Module not found error')
 # import maths # Provoque une erreur car le module 'maths' n'existe pas
import math  # Correct, le module 'math' existe

## Exemple 5 : AttributeError
print('\n Attribute error')
 # print(math.PI) # Provoque une erreur car 'PI' n'est pas un attribut de 'math'
print(math.pi)  # Correct, 'pi' est un attribut de 'math'

## Exemple 6 : KeyError
print('\n Key error')
users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
 # print(users['county'])  # Provoque une erreur car 'country' est mal orthographié
print(users['country'])  # Correct, 'country' est bien orthographié

## Exemple 7 : TypeError
print('\n Type error')
# 4 + '3'  # Provoque une erreur car on ne peut pas additionner un entier et une chaîne de caractères
print( 4 + int('3')) # Correct ou
print( 4 + float('3'))

# from math import power # Syntaxe incorrect, 'power' n'est pas un attribut de 'math'
from math import pow  # Correct, 'pow' est un attribut de 'math'
print(pow(2, 3))  # Correct, calcule 2^3

## Exemple 8 : ValueError
print('\n Value error')
# print(int('12a'))  # Provoque une erreur car '12a' n'est pas convertible en entier
print(int('12'))  # Correct, '12' est convertible en entier

## Exemple 9 : ZeroDivisionError
print('\n Zero division error')
# print( 1 / 0 )  # Provoque une erreur car on ne peut pas diviser par zéro
print( 1 / 2 )  # Correct, division par un nombre différent de zéro