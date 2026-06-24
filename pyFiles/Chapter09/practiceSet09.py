# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
'''
with open("poems.txt") as file:
    data = file.read()
    text = "".join(data)
    print("text:",text)
    if type(data) == str:
        if "twinkle" in data:
            print("Yes, the word twinkle present inside the data")
            print(data)
        else:
            print("No, the word twinkle is not present inside the data")
            print(data)
'''

# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previou Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

'''
import random

totalRun = 0

run = 0

runList = [0, 1, 2, 3, 4, 6]
print("You have got 1 over (6 balls) to play!")
while (run < 6):
    user = int(input(f"Score a run\nBall {run+1}:"))
    comp = random.choice(runList)
    print("Comp:",comp)

    if user in runList:
        if comp != user:
            totalRun += user
        else:
            print("You are Out!")
            break
    else:
        print("Invalid Score")

    run +=1

with open("Hi-score.txt", "r+") as file:
    score = int(file.read().strip())
    print("score:",score)
    if score > totalRun:
        print("Your Highest score is:", score)
        print("Your current score:",totalRun)
        file.seek(0)
        file.write(str(score))
    elif score < totalRun:
        print("Your Highest score is:", totalRun)
        print("Your current score:",totalRun)
        file.seek(0)
        file.write(str(totalRun))
    elif score == totalRun:
        print("Your current score is same as Highest score:",totalRun)

Note: we can also use random.randint(start_Range, end_range)
.randint(arg1, arg2) - Randomly select the value from arg1 to arg2.
'''

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year-old.

'''
import os
num = 2
if os.path.exists("tableFrom2_to_20"):
    os.system("rm tableFrom2_to_20/tableOf*")
    pass
elif os.path.exists("tableFrom2_to_20") == False: 
    os.system("mkdir tableFrom2_to_20")

while num <= 20:
    tableNum = 1
    while tableNum < 11:
        table = f"{num} * {tableNum} = {num * tableNum}\n"
        if tableNum < 11:
            with open(f"tableFrom2_to_20/tableOf{num}.txt","a") as file:
                file.write(table)
        
        tableNum +=1
    num +=1
'''

# 4. A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.
'''
import os
with open("word.txt", "r+") as file:
    word = file.read().strip()
    print(word)

    word = word.replace("Donkey", "#####")

    file.seek(0)
    file.write(word)
    file.truncate()
print("")
os.system("cat word.txt")
'''

# 5. Repeat program 4 for a list of such words to be censored.
'''
import os

with open("sensor.txt", "r") as file:
    content = file.read()

content = content.replace("Donkey", "*****")

with open("sensor.txt", "w") as file:
    file.write(content)

os.system("cat sensor.txt")
'''

# 6. Write a program to mine a log file and find out whether it contains ‘python’.

'''
with open("mining.txt") as file:
    for mine in file:
        if "python" in mine.lower(): 
            print("Yes python is present in mining.txt file")
            print(mine.strip())
        else:
            pass
'''

# 7. Write a program to find out the line number where python is present from ques 6
'''
with open("mining.txt") as file:
    for lineNum, mine in enumerate(file, start=1):
        if "python" in mine.lower():
            print("Yes python is present in mining.txt file")
            print(f"found at Line no {lineNum}: {mine.strip()}")
        else:
            pass
'''

# 8. Write a program to make a copy of a text file “this.txt”.
'''
#Part 1
import shutil

shutil.copy2("this.txt","this_cop1.txt")

# part2

with open("this.txt","r") as file:
    content = file.read()

with open("this_copy.txt", "w") as destination:
    destination = destination.write(content)
'''

# 9. Write a program to find out whether a file is identical and matches the content of another file
'''
with open("this.txt") as f1, open("this_copy.txt") as f2:
    if (f1.read() == f2.read()):
        print("Both file content is identical")
    else:
        print("Both files are different")
'''

# 10. Write a program to wipe out the content of a file using python.

'''
with open("this.txt", "r+") as f1:
    content = f1.read().strip()
    if content:
        f1.truncate(0)
    else:
        print("File is already empty")
'''

# 11. Write a python program to rename a file to “renamed_by_python.txt”.
'''
import os

if os.path.exists("this.txt"):
    os.rename("this.txt", "renamed_by_python.txt")
    print("this.txt file is renamed to renamed_by_python.txt")
else:
    print("this.txt is not exists at the path")
'''

with open("this_copy.txt") as f:
    content = f.read()

with open("this_new.txt", "w") as f:
    f.write(content)

