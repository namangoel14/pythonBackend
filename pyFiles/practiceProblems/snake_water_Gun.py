import random

print("Snake - Water - Gun")

n = int(input("Enter the number of rounds you want to play:"))

options = ['s','w','g']

rounds = 1

computer_win = 0

user_win = 0

while rounds <= n:

    print(f"Rounds:{rounds}\nSnake -  's'\nWater -  'w'\nGun -  'g'")

    try:
        player = input("Enter your option:")

    except EOFError as e:
        print(e)

    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input, try again\n")
        continue

    computer = random.choice(options)

    if computer == 's':
        if player == 'w':
            computer_win +=1
        elif player == 'g':
            user_win +=1

    elif computer == 'w':
        if player == 's':
            computer_win +=1
        elif player == 'g':
            user_win +=1
    elif computer == 'g':
        if player == 'w':
            computer_win +=1
        elif player == 's':
            user_win +=1
    

    if user_win > computer_win:
        print(f"You Win round {rounds}\n")
    elif computer_win > user_win:
        print(f"Computer win round {rounds}")
    else: 
        print("Draw!!\n")

    rounds +=1


if user_win > computer_win:
    print("Congratulations!! YOU WON!")
elif computer_win > user_win:
    print("You lose!")
else:
    print("Match Draw!!")
