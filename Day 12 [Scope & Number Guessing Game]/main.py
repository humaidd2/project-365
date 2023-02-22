import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
set_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

guesses = 0
chosen_number = int(random.choice(range(0, 100)))
print(chosen_number)

if set_difficulty == "easy":
    guesses = 10
else:
    guesses = 5

game_over = False

while not game_over:
    if guesses != 0:
        print(f"You have {guesses} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess > chosen_number:
            guesses -= 1
            print("Too High\nGuess Again")
        elif guess == chosen_number:
            print(f"Correct! The chosen number is {chosen_number}")
            game_over = True
        else:
            guesses -= 1
            print("Too Low\nGuess Again")
    else:
        game_over = True
        print(f"You have failed. The number is: {chosen_number}")

# from random import randint
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
#
# # Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#     """checks answer against guess. Returns the number of turns remaining."""
#     if guess > answer:
#         print("Too high.")
#         return turns - 1
#     elif guess < answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {answer}.")
#
#
# # Make function to set difficulty.
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
#
# def game():
#     print(logo)
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")
#
#     turns = set_difficulty()
#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#
#         # Let the user guess a number.
#         guess = int(input("Make a guess: "))
#
#         # Track the number of turns and reduce by 1 if they get it wrong.
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
#
# game()
