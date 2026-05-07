print("Grade Management System")

# student details

name = input("Enter student name: ")
roll_number = input("Enter student roll number: ")

# marks input

marks = []

maths = int(input("Enter marks for Mathematics: "))
marks.append(maths)

science = int(input("Enter marks for Science: "))
marks.append(science)

english = int(input("Enter marks for English: "))
marks.append(english)

social_studies = int(input("Enter marks for Social Studies: "))
marks.append(social_studies)

Language = int(input("Enter marks for Language: "))
marks.append(Language)

# Total and Average

total = sum(marks)
average = total / len(marks)

# Grade calculation
if average >= 90:
    grade = 'A1'
elif average >= 80:
    grade = 'A2'
elif average >= 70:
    grade = 'B1'
elif average >= 60:
    grade = 'B2'
elif average >= 50:
    grade = 'C1'
elif average >= 40:
    grade = 'C2'
elif average >= 33:
    grade = 'D'
else:
    grade = 'F'                    

# Display results

print("\nStudent Name:", name)
print("Roll Number:", roll_number)
print("Marks:")
print("Mathematics:", maths)
print("Science:", science)
print("English:", english)
print("Social Studies:", social_studies)
print("Language:", Language)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)

# End of the program