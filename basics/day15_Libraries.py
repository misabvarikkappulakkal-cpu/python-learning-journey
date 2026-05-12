# Libraries are a collection of pre-written code that can be used to perform specific tasks.
# They save time and effort by providing ready-made functions and tools.

# Built-in libraries

import math
import random
import datetime

print("Math Library:")
print("square root of 16:", math.sqrt(16))
print("pi:", math.pi)
print("factorial of 5:", math.factorial(5))

print("Random Library:")
print("random integer between 1 and 10:", random.randint(1, 10))
print("random choice from list:", random.choice(['apple', 'banana', 'cherry']))
print("random float between 0 and 1:", random.random())

print("Datetime Library:")
print("current date and time:", datetime.datetime.now())
print("current date:", datetime.date.today())
print("time difference (7 days):", datetime.timedelta(days=7))

print("custom library:")

def greet(name):
    print(f"Heyyy, {name}!")

greet("Bruce")
