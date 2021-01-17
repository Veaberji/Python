'''
Generates a random number in the user`s range and gets some attempts to guess it.
'''
# import modules to generate a number and quit from the app
from random import randint
from sys import exit


def enter(description):
    ''''Get an input from a user'''
    input_value = input(f"Enter {description} \n").lower()
    return input_check(input_value)


def input_check(input_value):
    ''''Check the input for a non-numeric value'''
    while not input_value.isdigit():
        check_for_quit(input_value)
        input_value = input("Incorrect input. Enter a positive integer.\n")
    return input_value


def check_for_quit(input_value):
    ''''Check the input for "quit"'''
    if input_value == "quit":
        print("You quit")
        exit()


print("Enter 'quit' for exit anytime")
while True:
    enter_range = enter("range size (from 1)")
    enter_number_of_attempts = enter("number of attempts")
    enter_guess_number = enter("guess number")

    generated_number = randint(1, int(enter_range))
    guess_number = int(enter_guess_number)
    number_of_attempts = int(enter_number_of_attempts)

    i = 1
    while i <= number_of_attempts:
        if generated_number != guess_number:
            print("Nope")
        else:
            print(f"You win! Number is {generated_number}")
            break
        if number_of_attempts == i:
            print(f"Hell no! It was {generated_number}")
            break
        i += 1
        enter_guess_number = enter("guess number")
        guess_number = int(enter_guess_number)
