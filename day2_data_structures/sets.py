# Example of sets in Python
a = {"Gopi", "Nani", "Karthik"}
b = {1,5,9}
print(a)
print(b)
print(type(a))
print(type(b))

#Set Operations
a = {3, 5, 7}
b = {8, 9, 10}

print(a | b)

# Type Casting Set
s = set((1, 2, 3, 4, 5))
print(s)
s = set("karthik")
print(s)

#Common Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)