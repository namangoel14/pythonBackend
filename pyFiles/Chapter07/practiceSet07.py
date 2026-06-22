
# 1. Write a program to print multiplication table of a given number using for loop.
number = 9

for i in range(1,11):
    print(number, "*", i, ":",number*i)
    # print(f"{number} x {i} = {number * i}")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
#l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]

for j in l:
    if "S" in j:
        print("Hi", j, "Good morning. \nNice to meet you.")
    '''
    if (name.startswith("S"))":
        print(f"Hello, {j}")
    '''


# 3. Attempt problem 1 using while loop.

number1 = 9
k=1
while (k < 11):
    print(number1, "*", k, ":",number1*k)
    k += 1


# 4. Write a program to find whether a given number is prime or not

primeNum = int(input("Enter a prime number:"))
factor = 0
for p in range(1, primeNum+1):
    if primeNum%p == 0:
        factor +=1
    if primeNum > 1:
        if (p == primeNum) and (factor > 2):
            print(primeNum, "is not a prime number.")
        elif (p == primeNum) and (factor == 2):
            print(primeNum, "is a prime number.")
    else:
        print(primeNum, "is not a prime number, because it has only 1 factor")


# 5. Write a program to find the sum of first n natural numbers using while loop.

naturalNum = int(input("Enter a natural number:"))
i=1
sumNum = 0
while i <= naturalNum:
    sumNum +=i
    if naturalNum >= 5:
        if (i == 5):
            print("Sum of first 5 natural numbers:", sumNum)
    elif (i==naturalNum) and (naturalNum<5):
        print("You don't enter the valid rangle of a Natural number")
    i +=1


# 6. Write a program to calculate the factorial of a given number using for loop.

fact = int(input("Enter a number to find out the FACTORIAL result:"))

result=1
for i in range(fact,0,-1):
    result = result*i
print("Factorial of",fact,"is:",result)

# 7. Write a program to print the following star pattern.
'''
*
***
***** for n = 3
'''
Number = int(input("Enter a Number:"))
num = 3
i = 1
count = 0

while (i<=Number):
    if count != num:
        if i%2 != 0:
            count +=1
            print("* " *  i)
    i += 1


# 8. Write a program to print the following star pattern:

'''
*
**
*** for n = 3
'''
num1 = 3
i=1
while (i<=3):
    print("* " *  i)
    i +=1

# 9. Write a program to print the following star pattern.

'''
* * *
* * for n = 3
* * *
'''
n=3
j = 1

list1 = []

while j <=n:
    listNum = int(input("Enter a number for pattern:"))
    list1.append(listNum)
    j +=1
    if len(list1) == n:
        for item in list1:
            print("* " * item)
    

# 10. Write a program to print multiplication table of n using for loops in reversed order.

table = int(input("Enter a number for the table:"))

for i in range(10, 0, -1):
    print(table,"*",i,":",table*i)


# STAR PATTERN1:
'''
  *
 ***
*****
'''

n = int(input("Enter the number:"))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")

# STAR PATTERN2: 
'''
***
* *
***
'''

n = int(input("Enter the number for star2:"))
for i in range(1, n+1):
    if (i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")

