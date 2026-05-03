students = [
    {"name": "Alice", "age": 20, "mark" : 95},
    {"name": "Bob", "age": 20, "mark": 85},
    {"name": "Charlie", "age": 19, "mark": 75}
]
for student in students:    print(student["name"])
topper = students[0]

for student in students:
    if student["mark"] > topper["mark"]:
        topper = student

print("Topper:", topper["name"], "-", topper["mark"])
# Here we have a list of dictionaries, where each dictionary represents a student with their name, age, and mark. We iterate through the list to find the student with the highest mark and print their name and mark.