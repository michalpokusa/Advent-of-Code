import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2024Day3Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        self.matches = pattern.finditer(self.input_data)

    def get_answer(self):
        total = 0

        for match in self.matches:
            number1 = match.group(1)
            number2 = match.group(2)

            total += int(number1) * int(number2)

        return total


class AdventOfCode2024Day3Part2(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
        self.matches = pattern.finditer(self.input_data)

    def get_answer(self):
        mul_enabled = True
        total = 0

        for match in self.matches:
            if match.group() == "do()":
                mul_enabled = True
                continue

            if match.group() == "don't()":
                mul_enabled = False
                continue

            if not mul_enabled:
                continue

            number1 = match.group(1)
            number2 = match.group(2)

            total += int(number1) * int(number2)

        return total


if __name__ == "__main__":
    answer = AdventOfCode2024Day3Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
