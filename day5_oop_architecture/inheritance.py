# Parent class
class Animal:
    def eat(self):
        print("This animal eats food")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Using the classes
d = Dog()
d.eat()   # Inherited method
d.bark()  # Own method


class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

c = Car()
c.start()
c.drive()

#single inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create object
d = Dog()

d.eat()   
d.bark()

#multilevel inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

# Create object
p = Puppy()

p.eat()   
p.bark()
p.play()

