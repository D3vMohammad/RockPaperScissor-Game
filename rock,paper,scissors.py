import random

com_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input=input("plz enter rock/paper/scissors, or q to quite: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("entred an invalid option")
        continue

    random_number = random.randint(0, 2)
    comp_pick = options[random_number]

    print("computer picked ", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors":
        print("You Won !")
        user_wins +=1

    elif user_input == "scissors" and comp_pick == "paper":
        print("You Won !")
        user_wins +=1

    elif user_input == "paper" and comp_pick == "rock":
        print("You Won !")
        user_wins +=1

    else :
        print("you lost !")
        com_wins +=1
        continue

print("you won : ", user_wins , "times.")
print("computer won : ", com_wins , "times.")
print("good bye")