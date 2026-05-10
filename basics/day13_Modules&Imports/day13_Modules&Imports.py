# Modules and Imports in Python

# Importing a whole module

import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# Importing specific functions from a module

import os
from random import randint, choice
print("Random integer between 1 and 10:", randint(1, 10))
print("Random choice from a list:", choice(['apple', 'banana', 'cherry']))

# Using alias names

import datetime as dt
print("Current date and time:", dt.datetime.now())

# Creating your own module
# Save the following code in a file named 'mymodule.py'
# def greet(name):
#     return f"Hello, {name}!"
# Now you can import and use the function from your module

import mymodule
message = mymodule.greet("James Bond")
print(message)

# Importing specific functions 
# from your module

from mymodule import greet
print(greet("Ethan Hunt"))

# Checking module content

print(dir(math))

# Built-in modules

import os

print("Current working directory:")
print(os.getcwd())

# List files in the current directory

print("Files in current directory:")
print(os.listdir())

# Note: The output of the above code will vary based on your current working directory and the files present in it.

# Output:
#Square root of 16: 4.0
#Value of pi: 3.141592653589793
#Random integer between 1 and 10: 1
#Random choice from a list: apple
#Current date and time: 2026-05-10 20:18:24.877017
#Hello, James Bond!
#Hello, Ethan Hunt!
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow',('radians'),('remainder'),('sin'),('sinh'),('sqrt'),('sumprod'),('tan'),('tanh'),('tau'),('trunc'),('ulp')]
#Current working directory:
#C:\Users\hp\python-learning-journey
#Files in current directory:
#['.git', '.gitignore', '.python-version', 'basics', 'MiniProjects', 'README.md', 'students.txt']