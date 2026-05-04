class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display_info(self):
        print(f"Name: {self.name}, Mark: {self.mark}")

    def is_topper(self):
        if self.mark > 90:
            print(self.name, "is a topper")    

# Creating an instance of the Student class
s1 = Student("Peter", 95)
s2 = Student("John", 85)

# Calling the method to display student information
s1.display_info() 
s2.display_info()

# Checking if students are toppers
s1.is_topper()
s2.is_topper()