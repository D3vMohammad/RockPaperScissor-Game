import random

com_wins = 0
user_wins = 0
draws = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Please enter rock/paper/scissor, or q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Entered an invalid option")
        continue

    random_number = random.randint(0, 2)
    comp_pick = options[random_number]

    print("Computer picked", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissor":
        print("You Won !")
        user_wins +=1

    elif user_input == "scissor" and comp_pick == "paper":
        print("You Won !")
        user_wins +=1

    elif user_input == "mitha" and comp_pick == "rock":
        print("You Won !")
        user_wins +=1

    elif user_input == comp_pick:
        print("draw !")
        draws +=1

    else :
        print("you lost !")
        com_wins +=1
        continue

print("\nYou won:", user_wins, "times.")
print("Computer won:", com_wins, "times.")
print("draws : ", draws, "times.")
print("Goodbye!")
