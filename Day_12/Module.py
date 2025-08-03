import random
import string

# 🔹 Level 1

# 1. Générer un ID utilisateur aléatoire de 6 caractères
def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

print("1.", random_user_id())  # Exemple : '1ee33d'

# 2. Générer plusieurs IDs selon les entrées utilisateur
def user_id_gen_by_user():
    num_chars = int(input("Nombre de caractères : "))
    num_ids = int(input("Nombre d'IDs à générer : "))
    chars = string.ascii_letters + string.digits
    ids = [''.join(random.choices(chars, k=num_chars)) for _ in range(num_ids)]
    return ids

# Exemple d'utilisation :
# print("2.", user_id_gen_by_user())  # Entrée utilisateur : 5 5

# 3. Générer une couleur RGB aléatoire
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print("3.", rgb_color_gen())  # Exemple : rgb(125,244,255)

# 🔹 Level 2

# 1. Générer une liste de couleurs hexadécimales
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors

print("2-1.", list_of_hexa_colors(3))  # Exemple : ['#a3e12f', '#03ed55', '#eb3d2b']

# 2. Générer une liste de couleurs RGB
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print("2-2.", list_of_rgb_colors(3))  # Exemple : ['rgb(5,55,175)', 'rgb(50,105,100)', 'rgb(15,26,80)']

# 3. Générer des couleurs selon le type demandé
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Type de couleur invalide"

print("2-3a.", generate_colors('hexa', 3))  # ➜ 3 couleurs hexadécimales
print("2-3b.", generate_colors('rgb', 2))   # ➜ 2 couleurs RGB

# 🔹 Level 3

# 1. Mélanger une liste
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

print("3-1.", shuffle_list([1, 2, 3, 4, 5]))  # Exemple : [3, 1, 5, 2, 4]

# 2. Générer 7 nombres uniques entre 0 et 9
def unique_random_numbers():
    return random.sample(range(10), 7)

print("3-2.", unique_random_numbers())  # Exemple : [0, 2, 5, 8, 1, 3, 6]
