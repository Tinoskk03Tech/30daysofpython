# 💻 Day 9 – Exercises

# 🔹 Level 1

# 1. Vérification de l'âge pour conduire
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Comparaison d'âge
my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    unit = "year" if diff == 1 else "years"
    print(f"You are {diff} {unit} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    unit = "year" if diff == 1 else "years"
    print(f"I am {diff} {unit} older than you.")
else:
    print("We are the same age.")

# 3. Comparaison de deux nombres
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# 🔹 Level 2

# 1. Attribution de notes
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score")

# 2. Détection de saison
month = input("Enter month: ").capitalize()
if month in ['September', 'October', 'November']:
    print("Season: Autumn")
elif month in ['December', 'January', 'February']:
    print("Season: Winter")
elif month in ['March', 'April', 'May']:
    print("Season: Spring")
elif month in ['June', 'July', 'August']:
    print("Season: Summer")
else:
    print("Invalid month")

# 3. Vérification de fruit
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print("Updated fruit list:", fruits)

# 🔹 Level 3

# 1. Dictionnaire de personne
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# a. Vérifier et afficher la compétence du milieu
if 'skills' in person:
    skills = person['skills']
    mid = len(skills) // 2
    print("Middle skill:", skills[mid])

# b. Vérifier si 'Python' est dans les compétences
if 'skills' in person:
    print("Has Python skill?", 'Python' in person['skills'])

# c. Déterminer le rôle du développeur
if 'skills' in person:
    s = set(person['skills'])
    if {'JavaScript', 'React'} <= s and len(s) == 2:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'} <= s:
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'} <= s:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# d. Vérifier mariage et pays
if person['is_marred'] and person['country'] == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} lives in Finland. He is married.")