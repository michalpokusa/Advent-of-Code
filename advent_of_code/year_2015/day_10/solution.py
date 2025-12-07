import re
from pathlib import Path

from advent_of_code import AdventOfCode


DEFAULT_EXAMPLE_INPUT_FILE_PATH = Path(__file__).parent.joinpath("example_input.txt")
DEFAULT_INPUT_FILE_PATH = Path(__file__).parent.joinpath("input.txt")


class AdventOfCode2015Day10Part1(AdventOfCode):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        parts = [
            group1
            for group1, group2 in re.findall(r"((\d)\2*)", self.input_data.strip())
        ]
        self.puzzle_input = [(len(part), part[0]) for part in parts]

    times = 40

    def look_and_say(self):
        temp = ""
        new_puzzle_input = []

        def optimize_temp(force: bool = False) -> str:
            nonlocal temp, new_puzzle_input
            while temp:
                if len(set(temp)) > 1 or force:
                    part = re.match(r"^(\d)\1*", temp)
                    new_puzzle_input.append((len(part.group(0)), part.group(0)[0]))
                    temp = temp[len(part.group(0)) :]
                else:
                    return

        for copies, digit in self.puzzle_input:
            temp += str(copies) + digit

            optimize_temp()

        optimize_temp(force=True)
        self.puzzle_input = new_puzzle_input

    def get_answer(self):
        for time in range(self.times):
            self.look_and_say()

        return sum(copies for copies, digit in self.puzzle_input)


class AdventOfCode2015Day10Part2(AdventOfCode2015Day10Part1):

    times = 50


if __name__ == "__main__":
    answer = AdventOfCode2015Day10Part2(DEFAULT_INPUT_FILE_PATH).get_answer()
    print(answer)
