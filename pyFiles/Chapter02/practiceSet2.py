## python variables
#
## Integer Variable
#a = 30
#
## float variable
#b = 11.2
#
## String variable
#_c = "Naman"
#
## Boolen Variable
#d = False
#
## None type variable
#e = None   
#
#print("none of e type: ", type(e))
## Arithmatic Operator
#
#"""
#1. Add ( + )
#2. Substractor ( - )
#
#"""
#print("\nFor OR Operator: \n")
#print("True or False: ", True or False)
#print("True or True: ", True or True)
#print("False or True: ",False or True)
#print("False or False: ", False or False)
#
#print("\nFor AND Operator: \n")
#print("True and False: ", True and False)
#print("True and True: ", True and True)
#print("False and True: ",False and True)
#print("False and False: ", False and False)
#
#
## Type of variable value
#
#a = 1
#b = 11.2
#c = "99.9"
#print("Type of a: ", type(a))
#print("Type of b: ", type(b))
#print("Type of c: ", type(c))
#intoString = str(b)
#intoFloat = float(c)
#print("intoString: ", type(intoString))
#print("intoFloat: ", type(intoFloat))
#intoInteger = int(b)
#print("intoInteger: ", type(intoInteger))
#intoString1 = float(c)
#
## input() function
#
#a = int(input("Enter your input first: "))
#b = float(input("Enter your input second: "))
#
#
#print("First input: ", a)
#print("Second input: ", b)
#print("First and Second: ", a + b)

# QA1 - Write a python program to add two numbers

inInteger = 30

inFloat = 10.5

sumOfTwoNumber = inInteger + inFloat

print("sum of both integer and float numbers: ", sumOfTwoNumber)

# Write a python program to find remainder when a number is divided by z

remainderOfNumber = inInteger % inFloat

print("Remainder: ", remainderOfNumber)

# Check the type of variable assigned using input() function.

inputValue1 = str(input("Enter any type of value1: "))
inputValue2 = float(input("Enter any type of value2: "))

typeOfValue1 = type(inputValue1)
typeOfValue2 = type(inputValue2)

print("Type of both value1 and value2: ", typeOfValue1, typeOfValue2)

#Use comparison operator to find out whether ‘a’ given variable is greater than ‘b’ or not.  Take a = 34 and b = 80

a = 34
b = 80

c = a > b

print("Is a is greater than b?", c)


# Write a python program to find an average of two numbers entered by the user.

firstNumber = int(input("Enter your first number: "))

secondNumber = int(input("Enter your second number: "))

AverageOfTwoNumbers = int((firstNumber + secondNumber) / 2)

print("The Average of first and second number is: ", AverageOfTwoNumbers)


# Write a python program to calculate the square of a number entered by the user

squareOfANumber = firstNumber**2

print("Square of a number is: ", squareOfANumber)
