import random
import sys


def enter(description):
    return input(f"Enter {description} \n").lower()


def check_for_quit(input_value):
    if input_value == "quit":
        print("You quit")
        sys.exit()


print("Enter quit for exit anytime")
while True:
    enter_range = enter("range size (from 1)")
    check_for_quit(enter_range)

    enter_number_of_attempts = enter("number of attempts")
    check_for_quit(enter_number_of_attempts)

    enter_guess_number = enter("guess number")
    check_for_quit(enter_guess_number)

    generated_number = random.randint(1, int(enter_range))
    guess_number = int(enter_guess_number)
    number_of_attempts = int(enter_number_of_attempts)

    i = 1
    while i <= number_of_attempts:
        if generated_number == guess_number:
            print(f"You win! Number is {generated_number}")
            break
        else:
            print("Nope")
        if number_of_attempts == i:
            print(f"Hell no! It was {generated_number}")
            break
        i += 1
        enter_guess_number = enter("guess number")
        check_for_quit(enter_guess_number)

        guess_number = int(enter_guess_number)
