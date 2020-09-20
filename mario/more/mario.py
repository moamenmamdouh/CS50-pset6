from cs50 import get_int


def main():
    height = get_int("Height: ")
    while height <= 0 or height > 8:
        height = get_int("Height: ")

    for i in range(height):
        leftspaces((height - 1) - i)
        leftside(i + 1)
        inspaces()
        rightside(i + 1)
        print()


def leftspaces(n):
    for i in range(n):
        print(" ", end="")


def inspaces():
    for i in range(2):
        print(" ", end="")


def leftside(n):
    for i in range(n):
        print("#", end="")


def rightside(n):
    for i in range(n):
        print("#", end="")


main()