# 1. Create a decorator uppercase_decorator that converts the return value of a function to uppercase.

def uppercase_decorator(func):
    def inner():
        return func().upper()
    return inner

@uppercase_decorator
def statement():
    return "Hello World"

print(statement())


# 2. Create a decorator add_greeting that adds "Hello " before the function's return value.

def add_greeting(func):
    def inner():
        return f"Hello {func()}"
    return inner

@add_greeting
def name():
    return "Naman"

print(name())

# 3. Create a decorator run_twice that executes the decorated function two times.


def run_twice(func):
    def inner():
        func()
        func()
    return inner

@run_twice
def sayHI():
    print("HI")

sayHI()

# 4. Create a decorator logger that prints the function name before execution.

def logger(func):
    def inner(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return inner

@logger
def sum(a, b):
    return a + b

print(sum(4, 5))

# 5. Create a decorator "timer" that measures how long a function takes to execute.
import time
def timer(func):
    def inner():
        start_time = time.time()
        print(start_time)
        result = func()
        end_time = time.time()
        print(end_time)
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        return result
    return inner

@timer
def slow_fun():
    time.sleep(2)
    print("Task Completed!")

slow_fun()

# 6. Create a decorator positive_only that allows execution only if all numeric arguments are positive.

def positive_only(func):
    def inner(*args, **kwargs):
        if all(num > 0 for num in args):
            return func(*args)
        else:
            return "Arguments are not positive"
    return inner


@positive_only
def add(a, b):
    return a + b

print(add(3, 9))
print(add(-9, -5))
print(add(3, -8))


# 7. Create a decorator repeat(n) that executes a function n times.

def repeat(*args):
    def decorator(func):
        def inner():
            for _ in range(args[0]):
                func()
        return inner
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()

# 8. Create a decorator cache_result that stores previously computed results and returns the cached value if the same arguments are used again.
def cache_result(func):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        print("cache:",cache)
        print("args:",args)
        return result
    return inner

a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
c = int(input("Enter the number c:"))
d = int(input("Enter the number d:"))
e = int(input("Enter the number e:"))
f = int(input("Enter the number f:"))
@cache_result
def square(a, b):
    print("Calculating...")
    return a * b


print(square(a, b))
print(square(c, d))
print(square(e, f))


print(square.__closure__[0].cell_contents)

# 9. Create a decorator require_admin that allows a function to execute only if the keyword argument role="admin" is provided.

def require_admin(func):
    def inner(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return func(*args, **kwargs)
        else:
            return f"Access Denied to {kwargs.get("role")} {args[0]}"
    return inner

@require_admin
def delete_user(username, role=None):
    print(f"Access granted to {username} as a {role}")
    return f"{username} Added"

print(delete_user("John", role="admin"))
print(delete_user("Mike", role="user"))
