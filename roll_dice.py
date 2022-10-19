import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll (1 - 6):\n"))

if guess == roll:
    print("you WIN $$$")
    print(f"The computer rolled a {roll}")
else:
    print("you LOSE :(")
    print(f"The computer rolled a {roll}")
