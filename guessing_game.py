#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 2022
# This program uses a break statement

import random


def main():
    # this function uses a break statement

    # input
    random_number = random.randint(0, 9)  # a number between 0 and 9
    positive_integer_as_string = input("Enter an integer: ")
    print("")

    # process & output
    try:
        positive_integer_as_number = int(positive_integer_as_string)
        for loop_counter in range(positive_integer_as_number):
            if loop_counter == random_number:
                print("{0} is correct".format(positive_integer_as_number))
                break
        if positive_integer_as_string > random_number:
            print(
                "{0} is greater than the random number.".format(
                    positive_integer_as_number
                )
            )
        else:
            print(
                "{0} is lower than the random number.".format(
                    positive_integer_as_number
                )
            )
    except ValueError:
        print("{0} is not an integer".format(positive_integer_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
