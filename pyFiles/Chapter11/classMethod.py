
class Person:
    country = "India"
    def employee(self):
        print(Person.country)
    @classmethod
    def greet(cls):
        print(cls.country)

class Manager(Person):
    country = "USA"
    def show_country(cls):
        print(cls.country)

Manager.greet()

data = "Naman-27"
name, age = data.split("-")
print(name,age)

