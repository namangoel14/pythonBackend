# Practice set06 for condition

# 1. Write a program to find the greatest of four numbers entered by the user.
'''
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
num4 = int(input("Enter a number:"))

if (num1 > num2) and (num1 > num3) and (num1 > num4):
    print(num1, "is greatest!")
elif (num2 > num1) and (num2 > num3) and (num2 > num4):
    print(num2, "is greatest!")
elif (num3 > num1) and (num3 > num2) and (num3 > num4):
    print(num3, "is greatest!")
elif (num4 > num1) and (num4 > num2) and (num4 > num3):
    print(num4, "is greatest!")
else:
    print("Invalid input!")
'''

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

'''
passing_criteria = int(input("Enter the Passing criteria:"))
total_passing_criteria = int(input("Enter the total passing criteria:"))
listOfSubject = []
subject1 = int(input("Enter the marks for Math subject:"))
listOfSubject.append(subject1)
percent_of_subject1 = (subject1/100)*100
subject2 = int(input("Enter the marks for Science subject:"))
listOfSubject.append(subject2)
percent_of_subject2 = (subject2/100)*100
subject3 = int(input("Enter the marks for English subject:"))
listOfSubject.append(subject3)
percent_of_subject3 = (subject3/100)*100

total_generated_marks = (percent_of_subject1 + percent_of_subject2 + percent_of_subject3)/len(listOfSubject)

if total_generated_marks >= total_passing_criteria:
    print("Math marks:", subject1)
    print("Science marks:", subject2)
    print("English marks:", subject3)
    print("Total Marks: ", total_generated_marks, "%")
    print("Total result: PASSED!")
    
elif total_generated_marks < total_passing_criteria:
    print("Math marks:", subject1)
    print("Science marks:", subject2)
    print("English marks:", subject3)
    print("Total Marks: ", total_generated_marks, "%")
    print("Total result: FAILED!")

else:
    print("Invalid input!")
'''

# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

'''
spam = input("enter a spam message to the user:")

if spam == "Make a lot of money":
    print("'Make a lot of money' is a spam message, Don't click on it!")
elif spam == "buy now":
    print("'buy now' is a spam message, Don't click on it!")
elif spam == "subscribe this":
    print("'subscribe this' is a spam message, don't click on it!")
elif spam == "click this":
    print("'click this' is a spam message, don't click on it!")
else:
    print("Not a spam message")

OR

if (("Make a lot of money" in spam) or ("buy now" in spam) or ("subscribe this" in spam) or ("click this" in spam)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
'''

# 4. Write a program to find whether a given username contains less than 10 characters or not.

'''
username = input("Enter your username:")

if username.replace(" ", "").isalpha(): 
    if len(username) <= 10:
        print(username, "contains", len(username), "characters, and it is under 10 character!")
    else:
        print(username, "contains", len(username), "characters, and it's under the valid range!")

else:
    print("you entered an Integer Charcter!")

'''

# 5. Write a program to calculate the grade of a student from his marks from the following
'''
scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D
<50 => F
'''

"""
grade = int(input("Enter your grades:"))

if grade >= 91 and grade <=100:
    print("Excellent!")
elif grade >= 81 and grade <=90:
    print("Your Grade is A")
elif grade >= 71 and grade <=80:
    print("Your Grade is B")
elif grade >= 61 and grade <=70:
    print("Your Grade is C")
elif grade >= 50 and grade <=60:
    print("Your Grade is D")
else:
    print("Your Grade is F")

"""

# 6. Write a program which finds out whether a given name is present in a list or not.
'''
givenList = []

givenName = input("Enter the name:")
givenList.append(givenName)
givenName = input("Enter the name:")
givenList.append(givenName)
givenName = input("Enter the name:")
givenList.append(givenName)
givenName = input("Enter the name:")
givenList.append(givenName)
print("List: ", givenList)
if len(givenList) > 0:
#    if givenList.index("Naman Goel") >= 0:
    if "Naman Goel"in givenList:
        print("Naman Goel is present in the list!")
    else:
        print("Naman Goel is not present in the list!")
else:
    print("The List is Empty!")
'''



# 7. Write a program to find out whether a given post is talking about “Harry” or not

post = input("Enter the post:")

if "harry" in post:
    print("This Post is talking about harry!")
else:
    print("This post is not talking about harry!")
