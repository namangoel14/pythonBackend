number1 = int(input("Enter a number1:"))
number2 = int(input("Enter a number2:"))

if (number2 == 0):
    raise ZeroDivisionError("Hey! We can't divide the value by zero")
else:
    print("Result:", number1/number2)

print("DONE")
