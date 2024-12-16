from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

strings = [string for string in input_data.split("\n") if string]


def is_nice(string: str) -> bool:

    # It contains at least three vowels (aeiou only)
    if sum(1 for letter in string if letter in "aeiou") < 3:
        return False

    # It contains at least one letter that appears twice in a row
    if not any(f"{letter}{letter}" in string for letter in string):
        return False

    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements
    if any(substring in string for substring in ["ab", "cd", "pq", "xy"]):
        return False

    return True


nice_strings = sum(1 for string in strings if is_nice(string))

print(nice_strings)
