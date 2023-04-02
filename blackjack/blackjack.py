import random
from blackjack_logo import *


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_list):
    if len(cards_list) == 2 and sum(cards_list) == 21:
        return 0
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(u_score, comp_score):
    if u_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Computer has blackjack. You lose!"
    elif u_score == 0:
        return "You have blackjack. You win!"
    elif u_score > 21:
        return f"Your score is {u_score}. You lose!"
    elif comp_score > 21:
        return f"Computer's score is {comp_score}. You win!"
    else:
        if u_score > comp_score:
            return f"Your score is {u_score}, computer's score is {comp_score}. You win!"
        else:
            return f"Your score is {u_score}, computer's score is {comp_score}. You lose!"


def play_game():
    print(logo_for_blackjack)

    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = 0
    computer_score = 0

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choose = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choose == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(u_score=user_score, comp_score=computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
