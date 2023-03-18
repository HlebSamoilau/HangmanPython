import random

from hangman_art import *
from hangman_words import *

display = []
end_of_the_game = False
lives = 6

chosen_word = str(random.choice(word_list))
word_len = len(chosen_word)

for i in range(word_len):
    display.append("_")

print(welcome)

print(steps[lives])
print(display)

while not end_of_the_game:
    letter_exists = False
    guess = input("You should guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed letter '{guess}'.")

    for position in range(word_len):
        if chosen_word[position] == guess:
            display[position] = guess
            letter_exists = True
    if not letter_exists:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
    print(steps[lives])
    print(display)
    if "_" not in display:
        end_of_the_game = True
        print("You win!!!")
    if lives == 0:
        end_of_the_game = True
        print(f"You lose!\nThe hidden word was: {chosen_word}")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

