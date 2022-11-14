#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 2022
# This program uses a break statement

import random


def main():
    # Finds if the chosen number from 0 to 9 is equal to the random number

    random_number = random.randint(0, 9)
    try:
        while True:
            user_input = input("\nEnter a number from 0 to 9: ")
            user_input_int = int(user_input)
            if user_input_int == random_number:
                print("\nCorrect!")
                print("The number was {}.".format(random_number))
                break
            elif user_input_int > random_number:
                print("\n{} is higher than the random number.".format(user_input))
            elif user_input_int < random_number:
                print("\n{} is lower than the random number.".format(user_input))
    except ValueError:
        print("\n{} is not an integer.".format(user_input))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
