# 1. Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.

try: 
    with (
        open("file1.txt") as f1,
        open("file2.txt") as f2,
        open("file3.txt") as f3
        ):
        pass
except Exception as e:
    print(e)

#print("End of the file")

# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(list1):
    if index > 1 and index < 8 and index % 2 != 0:
        print(index, item)

# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
"""
number = int(input("Enter the number for a table:"))
result = [number*item for item in range(1, 11)]
print(result)

"""

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
"""

try:
    num1 = int(input("Enter a number1:"))
    num2 = int(input("Enter a number2:"))
    if num2 == 0:
        raise ZeroDivisionError("Infinite")
    print(f"num1/num2: {num1/num2}")
except Exception as e:
    print(e)


print("Program4 Ends")
"""


# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt .
try:
    number = int(input("Enter the number for a table:"))
    with open("Tables.txt", "w") as t1:
        [t1.write(f"{number} * {item} = {number*item}\n") for item in range(1, 11)]
except Exception as e:
    print(e)







