try:
    with open("students.txt", "r") as file:
        data = file.readlines()
        for line in data:
            print(line.strip())
except FileNotFoundError:
    print("The file was not found. Creating a new file.")
    with open("students.txt", "w") as file:
        file.write("Cristiano Ronaldo\nLionel Messi\nNeymar Jr.\n")
    
    # When it runs  for the first time, it will create the file and write the names.
    # output = The file was not found. Creating a new file.
    # When it runs for the second time, it will read the file and print the names.
    # output = Cristiano Ronaldo
    #          Lionel Messi
    #          Neymar Jr.