# if else and elif condition 

a = 22

if a > 23:
    print("a is larger than 23")
elif a > 29:
    print("a is larger than 19")
else: 
    print("a is not larger than anyone!")

# Write a program to print yes when the age entered by the user is greater than or equal to 18.

age = int(input("Enter your age:"))

if age >= 18:
    print("yes")
else:
    print("no")


are_you_speaking_truth = True

if not are_you_speaking_truth:
    print("You are not speaking truth")

elif are_you_speaking_truth:
    print("Oh! You are speaking truth")
