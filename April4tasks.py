# ---------- INHERITANCE ----------

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def cute(self):
        print("Puppy is cute")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting, Dancing")

class Child(Father, Mother):
    def own_skills(self):
        print("Child: Coding")

class Vehicle:
    def run(self):
        print("Vehicle is running")

class Bike(Vehicle):
    def type(self):
        print("It's a bike")

class Car(Vehicle):
    def type(self):
        print("It's a car")

class ElectricCar(Car):
    def battery(self):
        print("Electric Car battery powered")

print("\n--- Inheritance ---")
puppy = Puppy()
puppy.sound()
puppy.bark()
puppy.cute()

cat = Cat()
cat.sound()
cat.meow()

ch = Child()
ch.skills()
ch.own_skills()

e_car = ElectricCar()
e_car.run()
e_car.type()
e_car.battery()


# ---------- METHOD OVERLOADING ----------
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

print("\n--- Method Overloading ---")
ol = OverloadDemo()
print("add(2, 3):", ol.add(2, 3))
print("add(1, 2, 3):", ol.add(1, 2, 3))
print("add():", ol.add())


# ---------- METHOD OVERRIDING ----------
class Parent:
    def show(self):
        print("Parent class")

class ChildOverride(Parent):
    def show(self):
        print("Child class overrides Parent")

print("\n--- Method Overriding ---")
co = ChildOverride()
co.show()


# ---------- ENCAPSULATION ----------
class Encapsulate:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def show(self):
        print("Inside Encapsulate class")

    def get_private(self):
        return self.__private

class Person:
    def __init__(self):
        self.name = "Yash"
        self._age = 23
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary!")

print("\n--- Encapsulation ---")
person = Person()
print("Name:", person.name)
print("Age:", person._age)
print("Salary:", person.get_salary())
person.set_salary(60000)
print("Updated Salary:", person.get_salary())


# ---------- POLYMORPHISM ----------
class Bird:
    def fly(self):
        print("Birds can fly")

class Airplane:
    def fly(self):
        print("Airplanes can fly")

def poly_fly(obj):
    obj.fly()

print("\n--- Polymorphism ---")
bird = Bird()
plane = Airplane()
poly_fly(bird)
poly_fly(plane)
