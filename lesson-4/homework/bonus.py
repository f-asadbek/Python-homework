import random
choices = ["rock", "paper", "scissors"]
score_a = 0
score_b = 0
while score_a < 5 and score_b < 5:
    a = input("Enter rock, paper, or scissors: ")
    b = random.choices(choices)
    if a == b :
        print("Draw!")
    elif (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper") :
        score_a += 1
        print("You won!")
    else :
        score_b += 1
        print("Computer won!")
    print(f"Your score : {score_a}, Computer score: {score_b}")
if a == 5:
    print("You won!")
else:
    print("Computer won!")