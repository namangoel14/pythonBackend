

def func1():
    print("Hello From python")


func1()

def _func1():
 pass

#message = _func1()
#print(message)
print(_func1())


# Write a program to greet a user with “Good day” using functions.

#user = input("Enter a user name:")
#def greet(user):
#    return f"Good day {user}"
#print(greet(user))


def greet(name = "stranger"):
    gr = "Hello " + name
    return gr

#print(greet("Naman"))
print(greet())


def names(*name):
    return name

listN = ["Naman","Goel","Iti","Eity","Nemo"]
print(names(listN))


def positional(name,/):
    for item in name:
        print(f"Hello {item}")

positional(listN)

def keywordOnly(*,names):
    return "Hello" +names + "GoodEvening" +names

print(keywordOnly(names="Naman"))

def my_func(**kids):
    print(f"His first name is {kids["fname"]} and last name is {kids["lname"]}")
    print(type(kids))
    print("All data:",kids)

my_func(fname="Naman", lname ="Goel")


def myfunction(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(myfunction(*numbers))

def myKeyword(fname, lname):
    return "Hello " +fname +" "+lname

person = {"fname": "Emil", "lname": "Refsnes"}
print(myKeyword(**person))


