print("string creation")

# string creation
a = "Bruce Wayne"
b = 'Batman'

print(a)
print(b)

print("\nstring indexing")

text = "Vengeance is mine"
print(text[0])  # V
print(text[1])  # e
print(text[2])  # n
print(text[3])  # g
print(text[4])  # e
print(text[5])  # a
print(text[6])  # n
print(text[7])  # c
print(text[8])  # e

print("\nstring slicing")

word = "Vengeance"
print(word[0:4])   # Veng
print(word[4:])    # eance
print(word[::-1])  # ecnaegneV

print("\nstring methods")

name = "Two Face"
print(name.upper())       # TWO FACE
print(name.lower())       # two face
print(name.capitalize())  # Two face
print(name.title())       # Two Face

msg = "   Gotham City   "
print(msg.strip())    # "Gotham City"
print(msg.lstrip())   # "Gotham City   "
print(msg.rstrip())   # "   Gotham City"

sentence = "I am the night"
print(sentence.split())  # ['I', 'am', 'the', 'night']

text = "The Joker is a criminal mastermind"
new_text = text.replace("Joker", "Riddler")
print(new_text)

print("\njoin")

words = ["dark", "knight", "rises"]
sentence = " >> ".join(words)
print(sentence)

result = "The Dark Knight".lower()
print(result)

print("\nchecking methods")

print("joker".isalpha())     # True
print("123".isdigit())       # True
print(" ".isspace())         # True
print("joker123".isalnum())  # True

print("\nf-strings")

name = "Robin"
age = 30

print(f"Hello, my name is {name} and I am {age} years old.")
print(f"I love Batman and it's been {2024 - 1939} years since his first appearance.")

print("\nescape characters")

print("He said, \"I am the night.\"")
print("This is a backslash: \\")
print("This is a newline:\nHello, World!")
print("This is a tab:\tHello, World!")

print("\nstring length")

text = "Hello, World!"
print(len(text))

print("\ncounting occurrences")

sentence = "The Joker is a criminal mastermind. The Joker is dangerous."
print(sentence.count("Joker"))

print("\nchecking start and end")

filename = "batman_logo.png"
print(filename.startswith("batman"))
print(filename.endswith(".png"))

print("\nstring immutability")

text = "Hello"

# text[0] = "h"

new_text = "h" + text[1:]
print(new_text)

print("\ncenter method")

title = "Batman"
print(title.center(20, "-"))

print("\nmini user input example")

username = input("Enter your name: ")

clean_username = username.strip().capitalize()

print(f"Formatted user: {clean_username}!")

print("\nreverse user input")

user_input = input("Enter a string to reverse: ")

reversed_input = user_input[::-1]

print(f"Reversed string: {reversed_input}")

print("\nword counter")

sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Number of words: {len(words)}")

print("\nend of string deep dive")