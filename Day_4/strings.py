# Question 1
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Question 2
print('Coding' + ' ' + 'For' + ' ' + 'All')

# Question 3
company = "Coding For All"

# Question 4
print(company)

# Question 5
print(len(company))

# Question 6
print(company.upper())

# Question 7
print(company.lower())

# Question 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Question 9
print(company[0:6])  

# Question 10
print(company.find("Coding"))
print(company.index("Coding"))

# Question 11
print(company.replace("Coding", "Python"))

# Question 12
phrase = "Python For Everyone"
print(phrase.replace("Everyone", "All"))

# Question 13
print(company.split())

# Question 14
techs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(techs.split(", "))

# Question 15
print(company[0])

# Question 16
print(len(company) - 1)

# Question 17
print(company[10])

# Question 18
sentence1 = "Python For Everyone"
acronym1 = ''.join([word[0] for word in sentence1.split()])
print(acronym1)

# Question 19
sentence2 = "Coding For All"
acronym2 = ''.join([word[0] for word in sentence2.split()])
print(acronym2)

# Question 20
print(company.index("C"))

# Question 21
print(company.index("F"))

# Question 22
sentence3 = "Coding For All People"
print(sentence3.rfind("l"))

# Question 23
s = 'You cannot end a sentence with because because because is a conjunction'
print(s.find("because"))

# Question 24
print(s.rindex("because"))

# Question 25
print(s[31:54])  # 'because because because'

# Question 26
print(s.find("because"))

# Question 27
print(s[31:54])  # répété par demande

# Question 28
print(company.startswith("Coding"))

# Question 29
print(company.endswith("coding"))

# Question 30
company_spaced = " Coding For All "
print(company_spaced.strip())

# Question 31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# Question 32
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))

# Question 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# Question 34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Question 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

# Question 36
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")