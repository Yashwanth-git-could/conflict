# ---------- INHERITANCE ----------

# 1. Single Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):  # Single Inheritance
    def bark(self):
        print("Dog barks")

# 2. Multilevel Inheritance
class Puppy(Dog):  # Multilevel: Animal -> Dog -> Puppy
    def cute(self):
        print("Puppy is cute")

# 3. Hierarchical Inheritance
class Cat(Animal):  # Hierarchical: Animal -> Dog & Cat
    def meow(self):
        print("Cat meows")

# 4. Multiple Inheritance
class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting, Dancing")

class Child(Father, Mother):  # Multiple
    def own_skills(self):
        print("Child: Coding")

# 5. Hybrid Inheritance (combination)
class Vehicle:
    def run(self):
        print("Vehicle is running")

class Bike(Vehicle):
    def type(self):
        print("It's a bike")

class Car(Vehicle):
    def type(self):
        print("It's a car")

class ElectricCar(Car):  # Hybrid: Vehicle -> Car -> ElectricCar
    def battery(self):
        print("Electric Car battery powered")

# ---------- METHOD OVERLOADING (using default args) ----------
class OverloadDemo:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            return a + b + c
        elif a and b:
            return a + b
        elif a:
            return a
        else:
            return 0

# ---------- METHOD OVERRIDING ----------
class Parent:
    def show(self):
        print("Parent class")

class ChildOverride(Parent):
    def show(self):
        print("Child class overrides Parent")

# ---------- ENCAPSULATION ----------
class Encapsulate:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def show(self):
        print("Inside class:", self.public, self._protected, self.__private)

    def get_private(self):
        return self.__private

# ---------- POLYMORPHISM ----------
class Bird:
    def fly(self):
        print("Birds can fly")

class Airplane:
    def fly(self):
        print("Airplanes can fly")

def poly_fly(obj):  # polymorphism via duck typing
    obj.fly()

# ---------- DRIVER CODE ----------

print("\n--- Inheritance ---")
puppy = Puppy()
puppy.sound()
puppy.bark()
puppy.cute()

cat = Cat()
cat.sound()
cat.meow()

ch = Child()
ch.skills()  # Demonstrates Method Resolution Order (MRO)
ch.own_skills()

e_car = ElectricCar()
e_car.run()
e_car.type()
e_car.battery()

print("\n--- Method Overloading ---")
ol = OverloadDemo()
print("add(2, 3):", ol.add(2, 3))
print("add(1, 2, 3):", ol.add(1, 2, 3))
print("add():", ol.add())

print("\n--- Method Overriding ---")
co = ChildOverride()
co.show()

print("\n--- Encapsulation ---")
enc = Encapsulate()
enc.show()
print("Accessing public:", enc.public)
print("Accessing protected:", enc._protected)
print("Accessing private via method:", enc.get_private())
# print(enc.__private)  # Will raise AttributeError

print("\n--- Polymorphism ---")
bird = Bird()
plane = Airplane()
poly_fly(bird)
poly_fly(plane)
