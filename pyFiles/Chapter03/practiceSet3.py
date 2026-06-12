## STRING in Python
#
#name = "naman"
#print("Length of a string: ", len(name))
#
#print("Include: ", name[0:3])
#print("name[1]: ", name[1])
#print("name[:4]", name[:4])
#print("name[1:]", name[1:])
#print("name[-4:-1]",name[-4:-1])
#print("name[:-1]",name[:-1])
#print("name[-7:]",name[-7:])
#print("name[-7:-1]",name[-7:-1])
#
#print("name[:5]",name[:5])
#
#print("name[:-4]",name[:-4])
#print("name[0:]",name[0:])
#
#
#
#print("name[1:4:2]: ",name[1:4:2])
#
#
## String() Function
#
## 1. len() in string
#
#print("Length of name: ", len(name))
##inputString = input("Enter any string: ")
##print("length of the string: ", len(inputString))
#
#
## 2. endswith() in string - checks the string ends with given text
#
#print("name ends with 'an': ", name.endswith("an"))
#
#print("name ends with rm: ", name.endswith("rm"))
#print("name starts with Na: ", name.endswith("Na"))
#
#
## 3. count() in string- counts total occurrences of a character.
#
#print("Total occurences of a: ", name.count("a"))
#print("Total occurences of n:", name.count("n"))
#print("Total occurences of r:", name.count("r"))
#
#
## 4. capitalize() in string - capitalizes the first character
#
#print("Capitalize: ", name.capitalize())
#
## 5. find() string- returns the index of first occurrence. 
#
#print("Find the index: ", name.find("m"))
#print("Find the index of aa:", name.find("aa"))
#print("Find the index of ma:", name.find("ma"))
#
#
## 6. replace(old word, new word) replaces the old word with the new word in the string.
#
#print("old word and new word: ", name.replace("n","N"))
#
#print("\tTAB " )
#print("\'Naman\'")
#print("\\Naman\\")
#
#name1 = "Namen Goel"
#
#print("slit() in string: ", name1.split())
#
## format() / f-string function in string
#
#print(f"My Name is {name1}")
#
#
## strip() function inn string - it remove extra spaces inside the string
#name3 = "     naman goel     "
#
#print("name3: ", name3)
#print("strip(): ", name3.strip())

# Practice set

#  1. Write a python program to display a user entered name followed by Good Afternoon using input() function.
"""
userName = input("Enter your name: ")
userComment = input("Enter your comment: ")

print(f"{userComment}, {userName}")
"""

# 2. Write a program to fill in a letter template given below with name and date.

"""
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""
"""
dearName = input("Enter the user Name: ")
selectedDate  = input("Entered the selected date: ")

letter = f"Dear {dearName},\nYour are selected!\n{selectedDate}"
print("Letter: ", letter)

or 

we can also use chaining method -> .replace().replace() - it means when we use the .replace() for the first time then from this first string after the replace of Name then we are replacing date as well after replace the pattern.
print(letter.replace("<|Name|>","Naman").replace("<|Date|>","01June2026"))
"""

# 3. Write a program to detect double space in a string.

"""
name = "  Naman  Goel  "

print("Double space: ", name.find("  "))

"""

# 4. Replace the double space from problem 3 with single spaces


"""
name = input("Enter the string: ")

print("Removed double space: ", name.replace("  "," "))
"""

# 5. Write a program to format the following letter using escape sequence characters.

'''
letter = "Dear Harry, this python course is nice. Thanks!"

'''

letter = "Dear Harry,\nthis \'python\' course is nice. \nThanks!"


print("escape sequence: ", letter)

