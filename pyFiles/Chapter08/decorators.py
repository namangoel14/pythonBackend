
def func1(func):
    def inner():
        print("Inner function")
        return func()
    return inner

@func1
def change1():
    return "Change1 function is called!"

@func1
def change2():
    return "Change2 function is called!"

print(change1())
print(change2())


def func2(func3):
    def inner5():
        print("Inner function for func2")
        return func3()
    return inner5

def change1(func4):
    def inner4():
        print("Inner function for change1")
        return func4()
    return inner4


@func2
@change1
def change3():
    return "Change3 function is called!"

print(change3())

