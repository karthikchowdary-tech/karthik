# Dictionary in Python
student = {
    "name": "Karthik",
    "age": 20,
    "course": "Ai"
}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])

# Example
employee = {
    "id": 101,
    "name": "Karthik",
    "salary": 30000
}

print("Employee Details")

for key, value in employee.items():
    print(key, ":", value)

## Accessing Dictionary Values
    student = {
    "name": "Karthik",
    "age": 22,
}
# Access values
print(student["name"])
print(student["age"])

# Dictionary to store student marks

student_marks = {
    "Maths": 95,
    "Science": 88,
    "English": 90
}
# Accessing marks
print("Maths Marks:", student_marks["Maths"])
print("Science Marks:", student_marks["Science"])
print("English Marks:", student_marks["English"])

# Nested Dictionary
students = {
    "student1": {
        "name": "Karthik",
        "age": 22,
        "course": "Ai"
    },
    "student2": {
        "name": "Nani",
        "age": 21,
        "course": "Data Science"
    }
}