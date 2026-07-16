# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

"""
To create a new virtual environment, 
Environment1:
pip install -m myenv1
We will install pandas in myenv1
source myenv1/bin/activate
myenv1/ -> pip install pandas==3.0.3
myenv1/ pip freeze > requirements.txt
Environment2:
pip install -m myenv2
source myenv2/bin/activate
myenv2/ -> pip install -r requirements.txt

"""

# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:

# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

"""
name = input("Enter the student name:")
marks = int(input("Enter the student marks: "))
phone_number = int(input("Enter the student phone number:"))

result = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_number)
print(result)
"""

# 3. A list contains the multiplication table of 7. Write a program to convert it to vertical string of same numbers.

"""
7
14
.
.
.

"""

table = [str(7*i) for i in range(1, 11)]

print("\n".join(table))

# 4. Write a program to filter a list of numbers which are divisible by 5.

number = [10, 2, 4, 5, 80, 58, 55]

result = filter(lambda x: x%5==0, number)
print(list(result))

# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

maximum = reduce(lambda x, y: x if x>y else y, number)
print(maximum)

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

"""
In the global invironment: pip freeze > requirement.txt
Now create a virtual environment -> pip install -m myenv
myenv/ pip install -r requirement.txt
It will install all the dependencies.
"""

# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
