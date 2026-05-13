# Debugging is the process of finding and fixing errors in your code.
# There are several types of errors that are:

# 1. Syntax Error

print("Hello World"
# this will give a syntax error because there is a missing parenthesis at the end of the line.

2. NameError

print(x)
# this will give a NameError because x is not defined.

3. TypeError

print(5 + "5")
# this will give a TypeError because you cannot add an integer and a string together.

4. IndexError

my_list = [1, 2, 3]
print(my_list[3])
# this will give an IndexError because there is no index 3 in the list (the last index is 2).

5. KeyError

my_dict = {"name": "Alice", "age": 30}
print(my_dict["gender"])
# this will give a KeyError because there is no key "gender" in the dictionary.

6. ValueError

int("abc")
# this will give a ValueError because you cannot convert the string "abc" to an integer.

6. ZeroDivisionError

print(5 / 0)
# this will give a ZeroDivisionError because you cannot divide a number by zero.

7. AttributeError

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# this will not give an error because the append method is a valid attribute of the list object. However, if you try to call a method that does not exist, such as my_list.push(4), it will give an AttributeError because there is no push method for lists.

8. FileNotFoundError

with open("non_existent_file.txt", "r") as file:
    content = file.read()
# this will give a FileNotFoundError because there is no file named "non_existent_file.txt" in the current directory.

9. ImportError

import non_existent_module
# this will give an ImportError because there is no module named "non_existent_module"

10. Average Function

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
print(average([1, 2, 3, 4, 5]))
# this will not give an error because the average function is defined correctly and can be called with

a list of numbers to calculate the average. 
However, if you try to call the average function with an empty list, such as average([]),
it will give a ZeroDivisionError because you cannot divide by zero when calculating the average.

11. Debugging Tools
There are several tools that can help you debug your code, such as:
- print statements: You can use print statements to check the values of variables at different points in your code.
- Debugger: Most programming environments have a built-in debugger that allows you to step through your
code line by line and inspect variables.
- Logging: You can use logging to record information about the execution of your code, which can
help you identify where errors are occurring.
- Unit Testing: Writing unit tests can help you catch errors early by testing individual functions or components
of your code for expected behavior.

# In conclusion, debugging is an essential part of the programming process, and understanding the different types of errors and how to use debugging tools can help you write more efficient and error-free code.
