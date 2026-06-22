import random

print("Welcome!\nLet's Play\nRock - Paper - Scissor\n")

print("Options:\nRock - r\nPaper - p\nScissor - s\n")

options = {
        "r": "rock",
        "p": "paper",
        "s": "scissor"
        }

user = input("Enter your option:")

chooseOption = options[user]
print("User input: ",chooseOption)
computer_input = random.choice(list(options))
random_value = options[computer_input]
print("Computer Input: ", random_value)

if random_value == 'rock' and chooseOption == 'paper':
    print("You Win!")
elif random_value == 'paper' and chooseOption == 'scissor':
    print("You Win")
elif random_value == 'scissor' and chooseOption == 'rock':
    print("You Win")
elif random_value == 'paper' and chooseOption == 'rock':
    print("You lose!")
elif random_value == 'scissor' and chooseOption == 'paper':
    print("You lose!")
elif random_value == 'rock' and chooseOption == 'scissor':
    print("You lose!")
elif random_value == chooseOption:
    print("Draw!")
else:
    print("Invalid input")


