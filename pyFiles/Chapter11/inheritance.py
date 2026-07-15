class Parent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello {self.name}"

class Child(Parent):
    def name1(self):
        return f"Welcome {self.name}"

p1 = Child("Naman")

print(p1.greet())
print(p1.name1())


class Rectangle:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

class Square(Rectangle):
    def __init__(self, length, breath):
        super().__init__(length,breath)

    def area(self):
        return self.length * self.breath


class Cube(Rectangle):
    def __init__(self, length, breath, height):
        super().__init__(length, breath)
        self.height = height

    def volume(self):
        return self.length * self.breath * self.height

a = Square(9, 10)
c = Cube(9, 10, 11)

print("Area: ", a.area())
print("Cube: ", c.volume())

