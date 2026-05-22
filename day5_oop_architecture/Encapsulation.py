class Student:
    def __init__(age, name, marks):
        age.name = name          # Public variable
        age.__marks = marks      # Private variable

    def get_marks(age):
        return age.__marks

    def set_marks(age, marks):
        if 0 <= marks <= 100:
            age.__marks = marks
        else:
            print("Invalid marks")

# Create object
s1 = Student("Karthik", 85)

# Access through methods
print("Name:", s1.name)
print("Marks:", s1.get_marks())

# Update marks
s1.set_marks(90)
print("Updated Marks:", s1.get_marks())