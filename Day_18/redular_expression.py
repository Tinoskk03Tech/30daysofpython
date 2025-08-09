import re
from collections import Counter

# -------------------------------
# Level 1 - Exercice 1 : Most frequent word
paragraph = '''I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love.'''

words = re.findall(r'\b\w+\b', paragraph.lower())
word_freq = Counter(words)
most_common_words = word_freq.most_common()
print("Most frequent words in paragraph:", most_common_words)
print("Most frequent word:", most_common_words[0])  # ('love', 6)

# -------------------------------
# Level 1 - Exercice 2 : Distance between furthest particles
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
numeric_points = list(map(int, points))
distance = max(numeric_points) - min(numeric_points)
print("Distance between furthest particles:", distance)  # 20

# -------------------------------
# Level 2 - Exercice 1 : Valid Python variable name
def is_valid_variable(name):
    return bool(re.match(r'^[a-zA-Z_]\w*$', name))

print("Valid variable tests:")
print("first_name:", is_valid_variable('first_name'))   # True
print("first-name:", is_valid_variable('first-name'))   # False
print("1first_name:", is_valid_variable('1first_name')) # False
print("firstname:", is_valid_variable('firstname'))     # True

# -------------------------------
# Level 3 - Exercice 1 : Clean text and find 3 most frequent words
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text)

def most_frequent_words(text):
    word = text.lower().split()
    freq = Counter(word)
    return freq.most_common(3)

cleaned_text = clean_text(sentence)
print("Cleaned text:\n", cleaned_text)
print("Top 3 frequent words:", most_frequent_words(cleaned_text))