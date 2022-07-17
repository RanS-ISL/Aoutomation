import math


def is_long(password: str) -> bool:
    """
    check if the str given long is at least 10.
    for example: "123456789" -> False
    :param password: the password the func will check(str)
    :return: bool
    """
    return len(password) > 9


def is_contain(password: str) -> tuple[bool, bool, bool, bool]:
    """
    check if the str given contain at least: 1 lowercase letter, 1 upper case letter and 1 digit
    and return the answer for each and also for all together.
    :param password: str
    :return: tuple(bool-result, bool-digit, bool-lower, bool-upper)
    """
    lower = False
    upper = False
    digit = False
    result = False
    for char in password:
        if char.isdigit():
            digit = True
        elif char.islower():
            lower = True
        elif char.isupper():
            upper = True
        if lower and upper and digit:
            result = True
    return result, digit, lower, upper


def is_valid(password: str):
    """
    check if the password strong enough and prints the results.
    for example: "eS444SRE" -> "PASSWORD ISN'T STRONG"
    :param password: str
    :return: none
    """
    if password[0:4] == "-f " and password[-1] == '"':
        f = open(password[4:-1], "r")
        password = f.read()
    lst = is_contain(password)
    dig = lst[1]
    low = lst[2]
    upp = lst[3]
    lon = is_long(password)
    if lon and lst[0]:
        print("\033[92mSuccess - your password IS STRONG enough")
    else:
        print("\033[91mYour password ISN'T STRONG enough, please see reasons, and try again.")
        if not lon:
            print("\033[91mYour password ISN'T long enough")
        if not dig:
            print("\033[91mYour password ISN'T contain at least one digit")
        if not low:
            print("\033[91mYour password ISN'T contain at list one lowercase letter")
        if not upp:
            print("\033[91mYour password ISN'T contain at list one Uppercase letter")
        exit(1)


def __main__():
    print("Please enter a password(at least 10 chars which include at least:"
          " 1 lower case letter, 1 upper case letter and 1 digit):")
    password = input()
    is_valid(password)


__main__()
