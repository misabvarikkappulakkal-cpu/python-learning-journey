try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = num1 / num2
    print("Result: ", num3)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")    

#calculator with exception handling

try:
    filename = input("Enter the filename: ")
    file = open(filename, 'r')    
except FileNotFoundError:
    print("File not found.")

else:
    content = file.read()
    print(content)
    file.close()
finally:
    print("Execution completed.")

#file handling with exception handling