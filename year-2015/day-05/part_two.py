from itertools import pairwise
from pathlib import Path

input_data = Path(__file__).parent.joinpath("input.txt").read_text()

strings = [string for string in input_data.split("\n") if string]


def is_nice(string: str) -> bool:
    unique_letters = set(string)

    # It contains a pair of any two letters that appears at least twice in the string without overlapping
    rule_one_met = False
    unique_pairs = set(pair for pair in pairwise(string))
    for pair in unique_pairs:
        if string.count("".join(pair)) > 1:
            rule_one_met = True
            break

    if not rule_one_met:
        return False

    # It contains at least one letter which repeats with exactly one letter between them
    rule_two_met = False
    for outside_letter in unique_letters:
        for inside_letter in unique_letters:
            if f"{outside_letter}{inside_letter}{outside_letter}" in string:
                rule_two_met = True
                break

    if not rule_two_met:
        return False

    return True


nice_strings = sum(1 for string in strings if is_nice(string))

print(nice_strings)
