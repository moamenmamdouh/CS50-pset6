from cs50 import get_string
import re


def main():
    card = get_string("Number: ")
    if len(card) == 15:
        if re.match("^3(4|7)", card):
            if checksum(card):
                print("AMEX")
            else:
                print("INVALID")
        else:
            print("INVALID")

    elif len(card) == 13:
        if re.match("^4", card):
            if checksum(card):
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")

    elif len(card) == 16:
        if re.match("^4", card):
            if checksum(card):
                print("VISA")
            else:
                print("INVALID")
        elif re.match("^5[1-5]", card):
            if checksum(card):
                print("MASTERCARD")
            else:
                print("INVALID")
        else:
            print("INVALID")

    else:
        print("INVALID")


def checksum(card):
    sum = 0
    for i in range(len(card) - 2, -1, -2):
        value = int(card[i]) * 2
        if value < 10:
            sum += value
        else:
            sum += (value % 10) + int(value / 10)

    if len(card) % 2 == 0:
        start = 1
    else:
        start = 0

    for i in range(start, len(card), 2):
        sum += int(card[i])

    if sum % 10 == 0:
        return True
    else:
        return False


main()

