#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program identifies a even or odd number

import constants


def main():
    # this function calculates the price

    # input
    print("This program calculates the amount you will pay.")
    print("One unit is $100.\n")
    unit_price = int(100)
    discount = int(0.10)
    user_number = input("Enter the amount of units you want to buy: ")

    # process and output
    try:
        integer_number = int(user_number)
        if integer_number >= 1000:
            sub_total = integer_number * unit_price
            plus_discount = sub_total - (sub_total * discount)
            total = plus_discount * constants.TAX
            print("You received a 10% discount. \nYour total is $ {0}".format(total))
        elif integer_number <= 1000:
            sub_total = integer_number * unit_price
            total = sub_total * constants.TAX
            print("Your total is ${0}.".format(total))
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thank You.")

    print("\nDone.")


if __name__ == "__main__":
    main()
