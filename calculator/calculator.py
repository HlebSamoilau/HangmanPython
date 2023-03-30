from calc_logo import *


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc_operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(calc_logo)
    first_number = float(input("What's the first number?: "))
    for operation in calc_operation:
        print(operation)
    if_continue = True
    while if_continue:
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calculation_function = calc_operation[operator]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {answer}")
        should_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation('q' for exit): ")
        if should_continue == "q":
            break
        elif should_continue == "n":
            if_continue = False
            calculator()
        elif should_continue == "y":
            first_number = answer


calculator()
