input_data = "hxbxwxba"

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"


# Passwords must include one increasing straight of at least three letters,
# like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# def includes_one
def password_includes_one_increasing_straight_of_three_letters(password: str) -> bool:
    for i in range(len(lowercase_letters) - 2):
        straight = lowercase_letters[i : i + 3]

        if straight in password:
            return True
    return False


# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for
# other characters and are therefore confusing.
def password_incudes_any_of(password: str, letters: str) -> bool:
    for letter in letters:
        if letter in password:
            return True
    return False


# Passwords must contain at least two different, non-overlapping pairs of letters,
#  aa, bb, or zz.
def password_contains_at_least_2_pairs_of_letters(password: str) -> bool:
    pairs_of_letters = 0
    for letter in lowercase_letters:
        if letter * 2 in password:
            pairs_of_letters += 1

        if pairs_of_letters >= 2:
            return True
    return False


def password_meets_requirements(password: str) -> bool:
    if not password_includes_one_increasing_straight_of_three_letters(password):
        return False

    if password_incudes_any_of(password, "iol"):
        return False

    if not password_contains_at_least_2_pairs_of_letters(password):
        return False

    return True


def password_to_number(password: str) -> int:
    number = 0
    for i, letter in enumerate(reversed(password)):
        number += lowercase_letters.index(letter) * (26**i)

    return number


def number_to_password(number: int) -> str:
    password = ""
    while number > 0:
        number, remainder = divmod(number, 26)
        password = lowercase_letters[remainder] + password

    return password


def get_next_password(current_password: str) -> str:
    current_password_number = password_to_number(current_password)

    while True:
        current_password_number += 1
        new_password = number_to_password(current_password_number)

        if password_meets_requirements(new_password):
            return new_password


# Part one
next_password = get_next_password(input_data)
print(next_password)

# Part two
next_password = get_next_password(next_password)
print(next_password)
