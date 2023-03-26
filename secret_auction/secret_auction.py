from secret_auction_logo import *

print("Welcome to the secret auction program.\n")
print(logo)

bidders_container = {}
other_bidders = True


def clear():
    print("\n" * 50)


def find_winner(bidders):
    winner = ""
    highest_bid = 0
    for bidder in bidders:
        if bidders_container[bidder] > highest_bid:
            highest_bid = bidders_container[bidder]
            winner = bidder
    print(f"Winner is {winner} with highest bid ${highest_bid}")


while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders_container[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
    if should_continue == "no":
        other_bidders = False
        find_winner(bidders_container)
    else:
        clear()
