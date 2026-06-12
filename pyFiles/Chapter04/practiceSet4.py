friends = ["Apple", "Akash", 2, 3.14, False, "Naman" ]

print(friends[0])

friends[0] = "Grape"

print(friends)
print("Mutable List:",friends[0])

print("slicing: ",friends[1:4])

# Python Methods

numbers = [5,10,99,1,4,45,33]
numbers.sort()
print("Sort:", numbers)
numbers.reverse()
print("reverse: ", numbers)
numbers.append("AppendValue")
print("Append: ", numbers)
numbers.insert(4, 115000)
print("Inserted Value: ",numbers)
print("Pop index value: ", numbers.pop(7))
print("Pop list: ", numbers)
numbers.remove(33)
print("Remove list: ", numbers)

# Tuple

a = (1, 2, 5, 6)

print("Type of a: ", type(a))

b = ()

print("Type of:", type(b))


c = (1, )

print("Type of c:",type(c))


d = (1, "Naman", 9, "Sky", 33, False, 22.54)

print("Type of d: ", type(d))

print("value of d[1]:", d[1])


# Tuple Method:

# count()

countValue = (2, 5, 9, 77, 10, 9)

print("countValue of 9: ", countValue.count(9))

# index()

indexValue = (2, 5, 9, 77, 10, 9)

print("indexValue of 77: ", indexValue.index(77))




# Practice set4

# 1. Write a program to store seven fruits in a list entered by the user


#fruit1 = input("Enter the fruit1:")
#fruit2 = input("Enter the fruit2:")
#fruit3 = input("Enter the fruit3:")
#fruit4 = input("Enter the fruit4:")
#fruit5 = input("Enter the fruit5:")
#fruit6 = input("Enter the fruit6:")
#fruit7 = input("Enter the fruit7:")

#listOfFruits = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
#We can also append the values like below:
# listOfFruits.append(fruit1)
#print("listOfFruits:", type(listOfFruits))
#print("listOfFruits:", listOfFruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

#student1_Marks = int(input("Enter a marks of student1:"))
#student2_Marks = int(input("Enter a marks of student2:"))
#student3_Marks = int(input("Enter a marks of student3:"))
#student4_Marks = int(input("Enter a marks of student4:"))
#student5_Marks = int(input("Enter a marks of student5:"))
#student6_Marks = int(input("Enter a marks of student6:"))
#
#marks = [student1_Marks, student2_Marks, student3_Marks, student4_Marks, student5_Marks, student6_Marks]
#
#print("List of marks: ", marks)
#marks.sort()
#print("Sorted list of marks: ", marks)

# 3. Check that a tuple type cannot be changed in python.

tupleType = tuple(input("Enter a tuple type values: ")) 

print("Changing tuple type to string: ", tupleType)
tupleType[1] = 4
print("tupleType[1]: 4", tupleType)

# 4. Write a program to sum a list with 4 numbers.

# We can also use build-in function in python -> print(sum(listNum))
number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
number3 = int(input("Enter number3:"))
number4 = int(input("Enter number4:"))

listNum = [number1, number2, number3, number4]

print("list with 4 numbers: ", listNum)

sumOfListNumbers = number1 + number2 + number3 + number4
listNum = [sumOfListNumbers]
print("Sum of list with 4 numbers: ", listNum)







# 5. Write a program to count the number of zeros in the following tuple:

# a = (7, 0, 8, 0, 0, 9)

countValue1 = (7, 0, 8, 0, 0, 9)

print("Count Values of zeros:", countValue1.count(0))








































