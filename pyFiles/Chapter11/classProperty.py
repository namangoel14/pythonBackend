
class MyClass:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

r = MyClass("BMW","BMW-X5-EV")
print(r.brand)
print(r.model)

r.model = "BMW M2"
print(r.model)


class Person:
    country = "India"
    def __init__(self):
        pass

p1 = Person()

p1.name = "Naman"
p1.age = 27
p1.salary = 4000000

print(p1.name)
print(p1.age)

del p1.salary

print(hasattr(p1, "name"))
print(hasattr(p1, "salary"))

print(getattr(p1, "name", "Not Found"))

setattr(p1, "age", 25)
print(p1.age)
print(p1.__dict__)
print(p1.country)
Person.country = "USA"
print(p1.country)
print(Person.country)
print(dir(p1))


class Person1():
    species = "Human"

    def __init__(self, name):
        self.name = name

p2 = Person1("Emil")
p3 = Person1("Tobias")

print(p2.name)
print(p3.name)

print(p2.species)
print(p3.species)


class String_fun:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person(name={self.name})"

ps = String_fun("Naman")
print(ps)
