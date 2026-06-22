# 1. Write a program using functions to find greatest of three numbers.


def greatest(num1, num2, num3):
    if num1 > num2 and num1>num3:
        print(f"{num1} is the greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest")
    elif num3 > num1 and num3 > num2:
        print(f"{num3} is the greatest")
    else: 
        print("All numbers are equal!")

num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))
greatest(num1, num2, num3)


# 2. Write a python program using function to convert Celsius to Fahrenheit.

def temperatureC_to_F(celsius):
    return (celsius * 1.8) + 32

cel = int(input("Enter the celsius temperature:"))
print("Celsius to Fahrenheit: ", temperatureC_to_F(cel), "degrees")


# 3. How do you prevent a python print() function to print a new line at the end.

def new_line_prevention():
    print("Hello", end=" ")
    print("World", end="")

new_line_prevention()

# 4. Write a recursive function to calculate the sum of first n natural numbers

def sumNum(n):
    if n == 0:
        return 0
    else: 
        return n + sumNum(n-1)

n = int(input("Enter the number to get the Natural number sum:"))
print("Sum of first",n," Natural numbers:",sumNum(n))


# 5. Write a python function to print first n lines of the following pattern.

'''
***
**
*
 for n = 3

And 
* * *
 * *
  *
'''

# With recursion:

def pattern(n):
    if (n==0):
       return
    print("*" * n)
    pattern(n-1)

'''
withour recursion:
def pattern(n):
    n1 = n
    while (n > 0):
        print(" " * (n1 - n), end="")
        print("* " * n)
        n -= 1
'''
patternNum = int(input("Enter the number for pattern generation:"))
pattern(patternNum)

# 6. Write a python function which converts inches to cms
inches = int(input("Enter the inches:"))

def inCMS(inc):
    return inc * 2.54

print(inches,"inches to cms:",inCMS(inches),"cm")

# 7. Write a python function to remove a given word from a list and strip it at the same time.

list1 = []
for item in range(1, 4):
    inputList = input("Enter the list:")
    list1.append(inputList)

def remove_strip(removeItem, listItem):
    if removeItem in listItem:
        listItem.remove(removeItem)
        print(f"{removeItem} is successfully removed from the list")
        print("updated List:",listItem)
        updatedList = removeItem.strip()
        print("strip list:", updatedList)
    else: 
        updatedList = removeItem.strip()
        print(f"{removeItem} is not in the given list")
        print("strip list:", updatedList)

'''
list2 = []
for item in range(1, 4):
    inputList = input("Enter the list:")
    list2.append(inputList)
def rem(removeItem, list2):
    n = []
    for item in list2:
        if not(item==removeItem):
            n.append(item.strip(removeItem))
    return n
'''
removeItem = input("Enter the Item which you want to remove for the list:")
remove_strip(removeItem, list1)
#print(rem("mo",list2))
    


# 8. Write a python function to print multiplication table of a given number.

multiplication = int(input("Enter the multiplication number:"))

def table(num):
    if num == 0:
        print("Please enter the value above zero!")
    else:
        for item in range(1, 11):
            print(f"{num} * {item} = {num*item}")

print("Table of",multiplication,": ")
table(multiplication)

