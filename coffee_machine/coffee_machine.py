from coffee_machine_resources import *

current_resources = resources


def get_coffee_types():
    types = ", ".join(MENU.keys())
    return types


def add_resources():
    for resource in current_resources:
        if resource == "water":
            current_resources[resource] += 300
        elif resource == "milk":
            current_resources[resource] += 200
        elif resource == "coffee":
            current_resources[resource] += 100


def print_report():
    for resource in current_resources:
        if resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {current_resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.capitalize()}: {current_resources[resource]}g")
        else:
            print(f"{resource.capitalize()}: ${current_resources[resource]}")


def get_ingredients_for_coffee(coffee_ingredients):
    for ingredient in coffee_ingredients:
        current_resources[ingredient] -= coffee_ingredients[ingredient]


def check_ingredients(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if current_resources[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient} in coffee machine.")
            return False
    return True


def check_cost(coffee_cost):
    input_money = 0
    while True:
        print("Please insert coins.")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        input_money = (input_money + (quarters * 25) + (dimes * 10) + (nickles * 5) + pennies) / 100
        if input_money >= coffee_cost:
            change = round((input_money - coffee_cost), 2)
            print(f"Here is ${change} in change.")
            current_resources["money"] += coffee_cost
            return True
        else:
            print(f"There are not enough money. You payed {round(input_money, 2)}, coffee costs {coffee_cost}.\n"
                  f"You should pay extra {coffee_cost - input_money}.")
            if input("Do you want to pay? Type 'y' or 'n': ") != "y":
                return False


def make_coffee(coffee_type):
    coffee_ingredients = MENU[coffee_type]["ingredients"]
    coffee_cost = MENU[coffee_type]["cost"]
    if check_ingredients(coffee_ingredients=coffee_ingredients) and check_cost(coffee_cost=coffee_cost):
        get_ingredients_for_coffee(coffee_ingredients=coffee_ingredients)
        print(f"Here is your {coffee_type} ☕️ Enjoy!")


def run_coffee_machine():
    while True:
        coffee_types = get_coffee_types()
        user_chose = input(f"What would you like? ({coffee_types}): ").lower()
        if user_chose == "report":
            print_report()
        elif user_chose == "off":
            break
        elif user_chose == "add resources":
            add_resources()
        else:
            make_coffee(coffee_type=user_chose)


run_coffee_machine()
