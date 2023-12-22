# RockPaperScissor-Game
play game with AI ;)

**Let's break down the code one line at a time:**

```python
import random
```
- Imports the `random` module for generating random numbers.

```python
com_wins = 0
user_wins = 0
```
- Initializes variables to track computer and user wins.

```python
options = ["rock", "paper", "scissors"]
```
- Defines a list of possible choices in the game.

```python
while True:
```
- Starts an infinite loop for the game.

```python
    user_input = input("Please enter rock/paper/scissors, or q to quit: ").lower()
```
- Prompts the user for input and converts it to lowercase for case-insensitive comparison.

```python
    if user_input == "q":
        break
```
- Breaks out of the loop if the user enters "q."

```python
    if user_input not in options:
        print("Entered an invalid option")
        continue
```
- Prints a message and continues to the next iteration if the user enters an invalid option.

```python
    random_number = random.randint(0, 2)
    comp_pick = options[random_number]
```
- Generates a random number to represent the computer's choice.

```python
    print("Computer picked", comp_pick + ".")
```
- Prints the computer's choice.

```python
    if user_input == "rock" and comp_pick == "scissors":
        print("You Won!")
        user_wins += 1
```
- Checks and prints the result if the user wins.

```python
    elif user_input == "scissors" and comp_pick == "paper":
        print("You Won!")
        user_wins += 1
```
- Checks and prints the result if the user wins.

```python
    elif user_input == "paper" and comp_pick == "rock":
        print("You Won!")
        user_wins += 1
```
- Checks and prints the result if the user wins.

```python
    else:
        print("You lost!")
        com_wins += 1
```
- Prints the result if the user loses and updates the computer's win count.

```python
print("You won:", user_wins, "times.")
print("Computer won:", com_wins, "times.")
print("Goodbye")
```
- Prints the final results and a farewell message after the user decides to quit.

- # draw option is added
