#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program identifies a even or odd number

from re import sub
import constants

def main():
    # this function calculates the price

    # input
    print("This program calculates the amount you will pay.")
    print("One unit is $100.")
    user_number = input("Enter the amount of units you want to buy: ")

    # process
    sub_total = user_number * constants.UNIT_PRICE
    plus_tax = sub_total * constants.TAX
    total = sub_total + plus_tax

    if user_number >= 1000:
        new_sub_total = total * 0.10
        new_total = total - new_sub_total
        print("You received a 10% discount. \nYour total is $ {0}".format(new_total))

    elif user_number <= 1000:
        print("Your total is ${0}.".format(total))
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
