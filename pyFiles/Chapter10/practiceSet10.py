# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:

    def __init__(self, company):
        self.company = company
        self.names = []
        self.ages = []
        self.techStacks = []

    def info(self, name, age, techStack):
        self.names.append(name)
        self.ages.append(age)
        self.techStacks.append(techStack)
        print(f"{self.company} employees:")
        print("Names: ", name)
        print("Ages: ", age)
        print("TechStack: ", techStack)

p = Programmer("Microsoft")
p.info("Naman", 27, "Full-Stack Engineer")
p.info("Mark", 18, "Software Engineer")
p.info("Nemo", 22, "Designer")

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,number):
        self.number = number
    def squareOfANumber(self):
        return f"Square of {self.number}: {self.number ** 2}"
    def cubeOfANumber(self):
        return f"Cube of {self.number}: {self.number ** 3}"
    def squareRootOfANumber(self):
        return f"Sqaure root of {self.number}: {self.number ** 0.5}"

Calculate = Calculator(25)
print(Calculate.squareOfANumber())
print(Calculate.cubeOfANumber())
print(Calculate.squareRootOfANumber())

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class MyClass:
    a = 10

obj = MyClass()

print("Before:")
print("class Attribute: ", MyClass.a)
print("Object Attribute: ", obj.a)

obj.a =  0 

print("After:")
print("class Attribute: ", MyClass.a)
print("Object Attribute: ", obj.a)

# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,number):
        self.number = number
    def squareOfANumber(self):
        return f"Square of {self.number}: {self.number ** 2}"
    def cubeOfANumber(self):
        return f"Cube of {self.number}: {self.number ** 3}"
    def squareRootOfANumber(self):
        return f"Sqaure root of {self.number}: {self.number ** 0.5}"
    @staticmethod
    def greet(name):
        return f"Hello {name}"

Calculate = Calculator(25)
print(Calculate.squareOfANumber())
print(Calculate.cubeOfANumber())
print(Calculate.squareRootOfANumber())
print(Calculate.greet("Naman"))

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import time
class Train:
    def __init__(self, startLocation, endLocation, startTime, endTime, trainStatus, fareInfo1, fareInfo2, seats1, seats2):
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.startTime = startTime
        self.endTime = endTime
        self.trainStatus = trainStatus
        self.fareInfo1 = fareInfo1
        self.fareInfo2 = fareInfo2
        self.seats1 = seats1
        self.seats2 = seats2
    def trainFareInfo(self):
        print("Indian Railways Train status:")
        print("Yoga Express!")
        print(f"Fare from {self.startLocation} and {self.endLocation}: {self.fareInfo1} per seat")
        print(f"{self.seats1} are available!")
        print("Shalimar Express!")
        print(f"Fare from {self.startLocation} and {self.endLocation}: {self.fareInfo2} per seat")
        print(f"{self.seats2} are available!")
    def ticketStatus(self):
        if self.trainStatus == True:
            print("Train is available!")
            print("Below are the trains and seats:")
            self.trainFareInfo()
        else:
            print("Train is notavailable!")
    def bookTicket(self):
        print(f"Your start Location: {self.startLocation} start at {self.startTime}")
        print(f"Your end Location: {self.endLocation} reach at {self.endTime}")
        print("Checking the seat availaibility.../")
        time.sleep(2)
        self.ticketStatus()

train = Train("Meerut Cant", "New Delhi", "12:02 PM", "1:10PM", True, 80, 76, 10, 5)
train.bookTicket()

# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” and see the effects.

class Self:
    def __init__(slf, name):
        slf.name = name
    def greet(slf):
        return f"Hello {slf.name} Welcome!"

sf = Self("Naman")
print(sf.greet())
