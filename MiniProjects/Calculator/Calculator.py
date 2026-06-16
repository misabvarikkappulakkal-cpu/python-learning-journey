while True:
    print("Enter the first number: ")
    num1 = float(input())
    print("Enter the second number: ")
    num2 = float(input())
    operation = input("Enter the operation (+, -, *, /) or 'exit': ")
    if operation == "exit":
        print("Exiting the calculator. Goodbye!")
        break   
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please try again.")
        continue
    print("Result: ", result)  