#mthod overriding

class Animal():
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals=[Dog(),Cat()]
for animal in animals:
    animal.sound()
    