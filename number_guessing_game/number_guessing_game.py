import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def get_difficult():
    chosen_difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if chosen_difficult == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_if_win(secret_number, is_guessed):
    if is_guessed:
        print(f"Congratulations! You got it! The answer was {secret_number}.")
    else:
        print(f"You've run out of guesses, you lose :( The answer was {secret_number}")


def start_new_game():
    if input("Do you want to try again? Type 'y' or 'n': ") == "y":
        run_game()
    else:
        print("Thank you for the game. Goodbye :)")


def run_game():
    welcome()
    secret_number = random.randint(1, 100)
    attempts = get_difficult()
    is_guessed = False
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == secret_number:
            is_guessed = True
            attempts = 0
        elif guess < secret_number:
            print("Too low.")
            attempts = attempts - 1
            if attempts > 0:
                print("Guess again")
        else:
            print("Too high.")
            attempts = attempts - 1
            if attempts > 0:
                print("Guess again")
    check_if_win(secret_number=secret_number, is_guessed=is_guessed)
    start_new_game()


run_game()

