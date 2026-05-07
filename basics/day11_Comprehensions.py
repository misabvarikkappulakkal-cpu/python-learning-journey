#Comprehensions are a concise way to create lists, dictionaries, or sets in Python. They allow you to generate new collections by applying an expression to each item in an iterable, optionally filtering items using a condition.

#List Comprehension

#Let's create a list of squares from 0 to 9

#Normal way
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Using list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#With Conditions

#Let's create a list of squares for even numbers from 0 to 9

#Normal way
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)  # Output: [0, 4, 16, 36, 64]

#Using list comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

#String example

#Let's create a list of uppercase letters from a string

#Normal way

input_string = "hello world"
uppercase_letters = []
for char in input_string:
    if char.isalpha():
        uppercase_letters.append(char.upper())
print(uppercase_letters)  # Output: ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

#Using list comprehension
uppercase_letters = [char.upper() for char in input_string if char.isalpha()]
print(uppercase_letters)  # Output: ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

#Conditional Expressions in Comprehensions

#Let's create a list of "Even" or "Odd" for numbers from 0 to 9

#Normal way
even_odd = []
for x in range(10):
    if x % 2 == 0:
        even_odd.append("Even")
    else:
        even_odd.append("Odd")
print(even_odd)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

#Using list comprehension with conditional expression
even_odd = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(even_odd)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

#Set Comprehension

#Let's create a set of unique squares from 0 to 9

#Normal way
unique_squares = set()
for x in range(10):
    unique_squares.add(x**2)
print(unique_squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

#Using set comprehension
unique_squares = {x**2 for x in range(10)}
print(unique_squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

#Dictionary Comprehension

#Let's create a dictionary where the keys are numbers from 0 to 9 and the values are their squares

#Normal way
squares_dict = {}
for x in range(10):
    squares_dict[x] = x**2
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}    

#Using dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#Nested Comprehensions

#Let's create a list of lists containing the multiplication table from 1 to 3

#Normal way
multiplication_table = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    multiplication_table.append(row)
print(multiplication_table)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#Using nested list comprehension
multiplication_table = [[i * j for j in range(1, 4)] for
                        i in range(1, 4)]
print(multiplication_table)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#Comprehensions are a powerful tool in Python that can help you write cleaner and more efficient code. They can be used to create lists, sets, and dictionaries in a single line of code, making your code more readable and concise. >>>> is this enough?