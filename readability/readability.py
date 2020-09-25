from cs50 import get_string
import re


def main():

    text = get_string("Text: ")
    index = colemanLiau(text)
    if index > 16:

        print("Grade 16+")

    elif index < 1:
        print("Before Grade 1")

    else:
        print(f"Grade {int(round(index))}")


def lettersCount(text):
    count = 0
    for i in text:
        if re.match("[a-zA-Z]", i):
            count += 1
    print(count)
    return count


def wordsCount(text):
    count = 0
    if len(text) > 0:
        count += 1

    for i in text:
        if re.match("\s", i):
            count += 1
    print(count)
    return count


def sentencesCount(text):
    count = 0
    for i in text:
        if (i == '.' or i == '!' or i == '?'):
            count += 1
    print(count)
    return count


def colemanLiau(text):
    letters = lettersCount(text)
    words = wordsCount(text)
    sentences = sentencesCount(text)
    L = letters * 100 / words
    S = sentences * 100 / words
    index = 0.0588 * L - 0.296 * S - 15.8
    print(index)
    return index


main()