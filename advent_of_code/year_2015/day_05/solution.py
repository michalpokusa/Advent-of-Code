from itertools import pairwise
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day5Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.strings = self.input_data.strip().split("\n")

    def is_nice(self, string: str) -> bool:
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

    def get_answer(self):
        return sum(1 for string in self.strings if self.is_nice(string))


class AdventOfCode2015Day5Part2(AdventOfCode2015Day5Part1):

    def is_nice(self, string: str) -> bool:
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


if __name__ == "__main__":
    answer = AdventOfCode2015Day5Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
