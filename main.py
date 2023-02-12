import random
print("Welcome to The Number Guessing Game!\nI'm thinking of a number between 1 to 100.")
choice = random.randint(1, 100)
# print(f"Pssst, the correct answer is {choice}")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if mode == "hard":
    lives = 5
else:
    lives = 10
print(f"You have {lives} attempts remaining to guess the number.")

# guess = int(input("Make a guess: "))

is_game = False
while not is_game:
    guess = int(input("Make a guess: "))
    if guess != choice:
        lives -= 1
    if guess > choice:
        print("Too high.")
        print(f"Guess again.\nYou have {lives} attempts remaining to guess the number.")
    elif guess < choice:
        print("Too low.")
        print(f"Guess again.\nYou have {lives} attempts remaining to guess the number.")
    elif guess == choice:
        is_game = True
        print(f"You got it! The answer was {choice}")
    if lives == 0:
        is_game = True
        print("You've run out of guess, you lose.")

# print(f"You got it! The answer was {choice}")
